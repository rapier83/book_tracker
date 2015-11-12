#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import re
import BookDBHandler

def get_soup(url):
	res = urllib.request.urlopen(url)
	html_doc = res.read()
	soup = BeautifulSoup(html_doc, "html.parser")
	return soup

def get_score_aladin(soup):
	t = soup.find("div",class_ = "ss_book_list")
	start_point = t.get_text().index(':') + 2
	score = int(t.get_text()[start_point:])
	return score

def get_score_yes24(soup):
	t = soup.find("p",class_ = "goods_rating")
	m = re.search('[0-9]+',t.get_text())
	score = int(m.group())
	return score

class score_collector:
	''' Colloect Sales Point form http://www.aladin.co.kr or http://www.yes24.com. In case of Kyobobook (site = 1) is 0 score. They don't provide any score.
	'''
	
	def __init__(self, book_id, site):
		self.url = BookDBHandler.get_url(book_id, site)
		self.res = urllib.request.urlopen(self.url)
		self.doc = self.res.read()
		self.soup = BeautifulSoup(self.doc, "html.parser")
		if site == 1:
			self.score = 0
			self.site_name = "Kyobo"
			return score
		if site == 2:
			self.score = self.get_yes24_score(self.soup)
			self.site_name = "Yes24"
		if site == 3:
			self.score = self.get_aladin_score(self.soup)
			self.site_name = "Aladin"

	def get_aladin_score(self, soup):
		t = soup.find("div",class_ = "ss_book_list")
		start_point = t.get_text().index(':') + 2
		score = int(t.get_text()[start_point:])
		return score

	def get_yes24_score(self, soup):
		t = soup.find("p",class_ = "goods_rating")
		m = re.search('[0-9]+',t.get_text())
		score = int(m.group())
		return score

s1 = score_collector(1,3)
s2 = score_collector(1,2)
print(s1.score)
print(s2.score)

