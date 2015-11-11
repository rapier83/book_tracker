#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import mysql.connector


# http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791195623624&orderClick=LEA&Kc=
# http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791195623617&orderClick=LAH&Kc=

# http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=69018367
# http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=69353271

# http://www.yes24.com/24/goods/22750663?scode=032&OzSrank=1
# http://www.yes24.com/24/goods/22793592?scode=032&OzSrank=1

# book_db = {'book_db':[{'title': '고흥, 고흥사람들', 'ISBN' : 9791195623624, 'aladin':69018367, 'yes24':22793592}, {'title': '하트마크', 'ISBN':9791195623617,' aladin' : 69353271, 'yes24' : 22750663}]}

def get_book_data(book, site):
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
		" FROM book_list WHERE id='" + str(book) + "'")

	cursor.execute(query)

	for (book_id, query_field) in cursor:
		target_book = book_id
		value = query_field
	
	cursor.close()
	cnx.close()

	return (target_book,value)

def get_page_url(book, site):
	kyobo_pre_url = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode='
	kyobo_sur_url = '&orderClick=LAH&Kc='
	aladin_pre_url = 'http://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Book&SearchWord='
	yes24_pre_url = 'http://www.yes24.com/searchcorner/Search?keywordAd=&keyword=&domain=ALL&qdomain=%C0%FC%C3%BC&Wcode=001_005&query='

	target, value = get_book_data(book,site)

	if site == 1:
		url = kyobo_pre_url + value + kyobo_sur_url
	if site == 2:
		url = yes24_pre_url + value
	if site == 3:
		url = aladin_pre_url + value
	return (url, site)

def get_score(url, site):
	#u = urllib.parse.urlparse(args[0])
	request = urllib.request.Request(url)
	res = urllib.request.urlopen(request)
	html_doc = res.read()
	soup = BeautifulSoup(html_doc,"html.parser")

	if site == 1:
		score = (0,site)
		return score
	if site == 2:
		return (0,site)
	if site == 3:
		t = soup.find("div",class_="ss_book_list")
		start_point = t.get_text().index(':') + 2
		score = int(t.get_text()[start_point:])
		print(score)

	return (score,site)





url, site = get_page_url(1,3)
get_score(url,site)
