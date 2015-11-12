#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import re
import BookDBHandler
def get_book_data(book_id, site):
	config = {
	'user': 'isaebooks',
	'password':'isae6200books',
	'host': 'root.cqrdsk303d9i.ap-northeast-1.rds.amazonaws.com',
	'database': 'trackers'
	}
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()

	query_field = "ISBN"	
	query = ("SELECT id, " + query_field + 
		" FROM book_list WHERE id='" + str(book_id) + "'")

	cursor.execute(query)

	for (db_book_id, query_field) in cursor:
		target_book = db_book_id
		value = query_field
	
	cursor.close()
	cnx.close()

	return (target_book,value)

def get_score(book_id, site):
	url = get_url(book_id, site)
	soup = get_soup(url)

	#if site == 1:
	#	score = (0,site)
	#	return score
	#if site == 2:
	#	score = get_score_yes24(soup)
	#if site == 3:
	s = score_collector(url, site)
	return (score,site)

def get_url(book_id, site):
	kyobo_pre_url = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode='
	kyobo_sur_url = '&orderClick=LAH&Kc='
	aladin_pre_url = 'http://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Book&SearchWord='
	yes24_pre_url = 'http://www.yes24.com/searchcorner/Search?keywordAd=&keyword=&domain=ALL&qdomain=%C0%FC%C3%BC&Wcode=001_005&query='

	target, value = get_book_data(book_id,site)

	if site == 1:
		url = kyobo_pre_url + value + kyobo_sur_url
	if site == 2:
		url = yes24_pre_url + value
	if site == 3:
		url = aladin_pre_url + value
	
	return url

def get_soup(url):
	res = urllib.request.urlopen(url)
	html_doc = res.read()
	soup = BeautifulSoup(html_doc, "html.parser")
	return soup

class score_collector:
	''' Colloect Sales Point form http://www.aladin.co.kr or http://www.yes24.com. In case of Kyobobook (site = 1) is 0 score. They don't provide any score.
	'''

	res = None
	doc = None
	soup = None
	score = None
	site = None
	
	def __init__(self, book_id, site):
		self.url = get_url(book_id, site)
		self.res = urllib.request.urlopen(self.url)
		self.doc = self.res.read()
		self.soup = BeautifulSoup(self.doc, "html.parser")
		self.t = self.soup

		self.score = self.abst_score(site)
		print("The score is: ",self.score)

	def abst_score(self,site):
		if site == 1:
			self.score = 0
			self.site = "Kyobo"
			return score
		if site == 2:
			t = self.soup.find('div', class_ = 'ss_book_list')
			self.site = "Aladin"

		if site == 3:
			t = self.soup.find('p', class_= 'goods_rating')
			self.site = "Yes24"

		m = re.search('[0-9]+',t.get_text())
		self.score = int(m.group())
		return score



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


s = score_collector(1,3)
print(s)
