#-*- coding: utf-8 -*-
#from bs4 import BeautifulSoup
import mysql.connector as sql

# http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791195623624&orderClick=LEA&Kc=
# http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791195623617&orderClick=LAH&Kc=

# http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=69018367
# http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=69353271

# http://www.yes24.com/24/goods/22750663?scode=032&OzSrank=1
# http://www.yes24.com/24/goods/22793592?scode=032&OzSrank=1

# book_db = {'book_db':[{'title': '고흥, 고흥사람들', 'ISBN' : 9791195623624, 'aladin':69018367, 'yes24':22793592}, {'title': '하트마크', 'ISBN':9791195623617,' aladin' : 69353271, 'yes24' : 22750663}]}

kyobo_pre_url = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode='
kyobo_sur_url = '&orderClick=LAH&Kc='
alddin_url = 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId='
yes24_pre_url = 'http://www.yes24.com/24/goods/'
yes24_sur_url = '?scode=032&OzSrank=1'

def get_book_data(book=1,site=1):
	config = {
	'user': 'isaebooks',
	'password':'isae6200books',
	'host': 'root.cqrdsk303d9i.ap-northeast-1.rds.amazonaws.com',
	'database': 'trackers'
	}
	cnx = sql.connect(**config)
	cursor = cnx.cursor()

	if site == 1:
		query_field = "kyobo"
	if site == 2:
		query_field = "yes24"
	if site == 3:
		query_field = "aladin"

	query = ("SELECT id, " + query_field + 
		" FROM book_list WHERE id='" + str(book) + "'")

	cursor.execute(query)

	for (book_id, query_field) in cursor:
		target_book = book_id
		value = query_field
	cursor.close()
	cnx.close()
	print (target_book, value)
	return (target_book,value)

def get_score(site=1):
	return


get_book_data(2,2)