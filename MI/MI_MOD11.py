#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# DB처리 공통모듈
#

import pymysql
from sqlalchemy import create_engine
from sqlalchemy import exc
import pandas as pd

pymysql.install_as_MySQLdb()
import MySQLdb


class MI_MOD11:
    def __init__(self):
        self.engine = create_engine("mysql+mysqldb://root:"+"Dkagh01!"+"@dooho.shop/dpweb?charset=utf8", encoding='utf-8')
        print(self.engine)
        self.conn = self.engine.connect()
        print(self.conn)

    # 전체테이블 Load
    def insert_batch_data_table(self, table_name, df):
        print(df)
        # for i in range(len(df)):
        #     try:
        #         print(df[i:i+1])
        #         df[i:i+1].to_sql(name=table_name, con=self.engine, if_exists='append')
        #     except exc.IntegrityError:
        #         pass  # or any other action
        df.to_sql(name=table_name, con=self.engine, if_exists='append')

    # 테이블 건별 Load
    def insert_data_table(self, table_name, df):
        # print(df)
        for i in range(len(df)):
            try:
                print(df[i:i+1])
                df[i:i+1].to_sql(name=table_name, con=self.engine, if_exists='append')
            except exc.IntegrityError:
                pass  # or any other action
        # df.to_sql(name=table_name, con=self.engine, if_exists='append')

    # 전체테이블 SELECT
    def select_batch_data_table(self, table_name):
        df = pd.read_sql_table(
            table_name,
            con=self.engine
        )
        return df

    # 테이블 건별 SELECT
    def select_data_table(self, myquery):

        df = pd.read_sql(myquery, self.conn)
        # print(df)
        return df

    # 테이블 건별 SELECT
    def update_data_table(self, table_name, df):

        df["co_region"] = "현대오토에버"
        print(df)

        df.to_sql(name=table_name, con=self.engine, if_exists='append')

        # print(df)
        return df


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



