# -*-coding:utf8-*-

import requests
import json
import random
import pymysql
import sys
import datetime
import time
from imp import reload
from multiprocessing.dummy import Pool as ThreadPool
import urllib


def insert():
    try:
        # Please write your MySQL's information.
        conn = pymysql.connect(host='35.236.132.111',
                               user='root',
                               passwd='123456',
                               db='my',
                               charset='utf8')
        cur = conn.cursor()
        cur.execute('INSERT INTO bilibili_user_info(mid, name, sex, rank, face, regtime, spacesta, \
                    birthday, sign, level, OfficialVerifyType, OfficialVerifyDesc, vipType, vipStatus, \
                    toutu, toutuId, coins, following, fans ,archiveview, article) \
        VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",\
                "%s","%s","%s","%s","%s", "%s","%s","%s","%s","%s","%s")'
                    %
                    (1, 'a', 'b', 'c', 'c', 'v', 'c', \
                    'c', 'c', 'c', 'c', 'c', 'c', 'c', \
                    'c', 1, 1, 1, 1 ,1, 1))
        conn.commit()
    except Exception as e:
        print(e)


# insert()

urls = ['http://www.yahoo.com', 'http://www.reddit.com']
results = map(urllib.request.urlopen, urls)