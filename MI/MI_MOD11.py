#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# DB처리 공통모듈
#

import pymysql
import requests
from bs4 import BeautifulSoup
from time import sleep
import re

class MI_MOD11:
    def __init__(self, host, id, pw, db_name):
        self.conn = pymysql.connect(host=host, user= id, password=pw, db=db_name,charset='utf8')
        self.curs = self.conn.cursor()

    def insert_total(self,total):
        sql = 'INSERT INTO entire_nodes (count_of_nodes) VALUES (%s)'
        self.curs.execute(sql,(total,))
        self.conn.commit()


# #  main.py
# url = 'https://www.ethernodes.org/network/1'
#
# INTERBAL = 60  # 1초
#
# if __name__=='__main__':
#     regex = re.compile(r'Total(.*\d)\s')
#     mysql_controller = MysqlController('localhost','root','Dkagh01!','dpweb')
#
#     while True:
#         res = requests.get(url)
#         if res.status_code == 200:
#             soup = BeautifulSoup(res.text, 'html.parser')
#             items = soup.find_all('li')
#
#             for item in items:
#                 result = regex.search(item.text)
#                 if result:
#                     mysql_controller.insert_total(result.groups(1)[0])
#                     sleep(INTERBAL)
#



