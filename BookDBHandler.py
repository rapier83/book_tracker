#-*- coding: utf-8 -*-
import mysql.connector
from datetime import datetime, date

config = {
	'user': #id,
	'password': #password,
	'host': #address,
	'database': #db'
	}

def get_book_data(book_id):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	# target = None
	# value = None

	query_field = "ISBN"	
	query = ("SELECT id, " + query_field + 
		" FROM book_list WHERE id='" + str(book_id) + "'")
	cursor.execute(query)

	for query_field in cursor:
		target, value = query_field

	cursor.close()
	cnx.close()

	return value

def write_score(_id, score):

	if type(score) is not dict:
		raise TypeError('The score argument is not "dict" type')
	
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()

	insert_query = ("INSERT INTO `score` (`book_id`, `time`, `kyobo_score`, `aladin_score`, `yes24_score`) " + "VALUES (%s, %s, %s, %s, %s)")
	
	d = (_id, datetime.now(), score['kyobo'], score['yes24'], score['aladin'])
	
	cursor.execute(insert_query, d)
	cnx.commit()

	cursor.close()
	cnx.close()

def get_url(book_id):
    kyobo_pre_url = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode='
    aladin_pre_url = 'http://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Book&SearchWord='
    yes24_pre_url = 'http://www.yes24.com/searchcorner/Search?keywordAd=&keyword=&domain=ALL&qdomain=%C0%FC%C3%BC&Wcode=001_005&query='
    isbn = get_book_data(book_id)
    url = {
    'kyobo': kyobo_pre_url + str(isbn),
    'yes24': yes24_pre_url + str(isbn),
    'aladin': aladin_pre_url + str(isbn)
    }
    return url


