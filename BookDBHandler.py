#-*- coding: utf-8 -*-
import mysql.connector

config = {
	'user': 'isaebooks',
	'password':'isae6200books',
	'host': 'root.cqrdsk303d9i.ap-northeast-1.rds.amazonaws.com',
	'database': 'trackers'
	}

def get_book_data(book_id, site):
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

def write_score(book_id, site, score):

	query = 'INSERT INTO `trackers`.`score` (`book_id`, `time`, `kyobo_score`, `aladin_score`, `yes24_score`) VALUES (` +
		'`' + book_id + '`, ' +
		'`' + time + + '`, ' +
		'`' + kyobo_score + '`, ' +
		'`' + aladin_score + '`)'


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