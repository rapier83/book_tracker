#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import re
import BookDBHandler

class score_handler:
	''' Colloect Sales Point form http://www.aladin.co.kr or http://www.yes24.com. In case of Kyobobook (site = 1) is 0 score. They don't provide any score.
	'''
	
	def __init__(self, book_id):
		self.url = BookDBHandler.get_url(book_id)
		self._id = book_id
		self.keys = tuple(self.url.keys())
		self.web_data = dict()
		self.score = dict()
		for key in self.keys:
			self.web_data[key] = {
			'url': self.url[key]
			}

		for key in self.keys:
			self.web_data[key]['doc'] = urllib.request.urlopen(self.web_data[key]['url']).read()
			self.web_data[key]['soup'] = BeautifulSoup(self.web_data[key]['doc'], "html.parser")
			self.score[key] = self.get_score(key, self.web_data[key]['soup'])
		#self.soup = BeautifulSoup(self.doc, "html.parser")
		
	def get_score(self, site, soup):
		s = None
		if site == 'kyobo':
			score = 0
			return score
		if site == 'aladin':
			t = soup.find("div",class_ = "ss_book_list")
			start_point = t.get_text().index(':') + 2
			s = t.get_text()[start_point:]
		if site == 'yes24':	
			t = soup.find("p",class_ = "goods_rating")
			m = re.search('[\d,]+',t.get_text())
			s = m.group()
		score = self.remove_comma(s)
		return score

	def get_yes24_score(self, soup):
		t = soup.find("p",class_ = "goods_rating")
		m = re.search('[\d,]+',t.get_text())
		score = int(m.group())
		return score
	
	def remove_comma(self,st):
		return int(st.replace(',','').strip())

	def show_score(self):
		print ("Kyobo : Not Count\nYes24:%10d\nAladin:%10d".format())

	def input_score(self):
		BookDBHandler.write_score(self._id, self.score)

s = score_handler(1)
s.input_score()