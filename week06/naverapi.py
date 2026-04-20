# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json

client_id =  'bj6aHRnJgsD10bL_E38K'
client_secret = '1khTglJB6Q'

def main():

    node = 'news'                                             # 크롤링할 대상
    srcText = input('검색어를 입력하세요: ')

    