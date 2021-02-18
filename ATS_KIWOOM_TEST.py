
#
# 작성일 : 2021-01-20
# 작성자 : Daniel Nho
# MAIN 모듈
#

import sys
from PyQt5.QtWidgets import *
from MI import MI_MOD02
from ST import ST_MOD01
from CM import CM_MOD01
from MI import MI_MOD11
import threading
import time
from pandas import DataFrame
import datetime


class ATS_KIWOOM_TEST:
    def __init__(self):
        print("__init__")

        self.mi_mod02 = MI_MOD02.MI_MOD02()                 # 키움증권 공통모듈
        self.st_mod01 = ST_MOD01.ST_MOD01(self.mi_mod02)    # 주식모듈
        self.cm_mod01 = CM_MOD01.CM_MOD01(self.mi_mod02)    # 고객모듈

    def run(self):
        print("run!!")
        self.cm_mod01.login()  # 로그인
        #######################################################################
        # 1) 종목 코드리스트 가지고옴
        # self.st_mod01.get_code_list()
        #######################################################################

        #######################################################################
        # 2) 계좌번호 가지고온다
        # account = self.cm_mod01.get_account_list()
        # print("계좌번호 : " + account)
        #######################################################################

        #######################################################################
        # 3) 급등주 파악한다
        # self.st_mod01.get_code_list()
        # buy_list = []
        # num = len(self.st_mod01.kosdaq_codes)  # 코스닥
        # for i, code in enumerate(self.st_mod01.kosdaq_codes):
        #     print(i, '/', num, '/', code)
        #     if self.st_mod01.check_speedy_rising_volume(code):
        #         buy_list.append(code)
        # # self.st_mod01.update_buy_list(buy_list) # 급등리스트 파일에 쓴다
        #
        # num = len(self.st_mod01.kospi_codes)  # 코스피
        # for i, code in enumerate(self.st_mod01.kospi_codes):
        #     print(i, '/', num, '/', code)
        #     if self.st_mod01.check_speedy_rising_volume(code):
        #         buy_list.append(code)
        #######################################################################


        #######################################################################
        # 4) 잔고를 파악한다
        # accno = self.mi_mod02.get_login_info("ACCNO")
        # accno_array = accno.split(';')
        # print(accno_array)
        # accno = accno_array[0]
        # self.st_mod01.get_account_amount(accno)
        #######################################################################


        #######################################################################
        # 5) 예수금 잔고를 파악한다
        # accno_list = self.cm_mod01.get_account_list()
        # accno = accno_list[0]
        # self.st_mod01.get_yesugum_amount(accno)

        #######################################################################
        # 6) 기업정보 가지고온다
        # mi_mod11 = MI_MOD11.MI_MOD11()
        # df = mi_mod11.select_batch_data_table("st_tb_stock_info")
        # print(df)
        # print(len(df))
        #
        # # 에러났을 때 그 이후부터 수행
        # df = df[df['st_cd'] > '103590']
        # df.reset_index(drop=True, inplace=True)
        # print(df)
        # print(len(df))
        #
        # for i in range(len(df)):
        #     # print(df.loc[i]["st_cd"])
        #     self.st_mod01.get_stock_info(df.loc[i]["st_cd"])
        #######################################################################

        #######################################################################
        # 7) 호가정보 가지고온다
        st_dt = '024810'
        while True:
            self.st_mod01.get_level_price_info(st_dt)
            # time.sleep(1)



if __name__ == "__main__":
    print("__main__")
    app = QApplication(sys.argv)
    ats = ATS_KIWOOM_TEST()
    # threading.Timer(4, ats.run).start()
    ats.run()
