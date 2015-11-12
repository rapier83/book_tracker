#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import re
import BookDBHander

class score_collector:
    ''' Colloect Sales Point form http://www.aladin.co.kr or http://www.yes24.com. In case of Kyobobook (site = 1) is 0 score. They don't provide any score.
    '''

    res = None
    doc = None
    soup = None
    score = None
    site = None
    def __init__(self, book_id, site):
        self.url = BookDBHander.get_url(book_id, site)
        self.res = urllib.request.urlopen(self.url)
        self.doc = self.res.read()
        self.soup = BeautifulSoup(self.doc, "html.parser")
        self.t = self.soup.title

    def get_title(self):
        return self.t
