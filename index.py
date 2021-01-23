
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
import time
from pandas import DataFrame
import datetime


class ATS:
    def __init__(self):
        print("__init__")
        # 키움증권 공통모듈
        self.mi_mod02 = MI_MOD02.MI_MOD02()  # 키움 공통모듈
        self.mi_mod02.comm_connect()  # 로그인

        # 주식모듈
        self.st_mod01 = ST_MOD01.ST_MOD01(self.mi_mod02)

        # 고객모듈
        self.cm_mod01 = CM_MOD01.CM_MOD01(self.mi_mod02)


    def run(self):
        print("run!!")

        # 코드리스트 가지고옴
        self.st_mod01.get_code_list()

        # 계좌번호 가지고온다
        account = self.cm_mod01.get_account_list()
        print("계좌번호 : " + account)

        # 급등주 파악한다
        buy_list = []
        num = len(self.st_mod01.kosdaq_codes)
        for i, code in enumerate(self.st_mod01.kosdaq_codes):
            print(i, '/', num, '/', code)
            if self.st_mod01.check_speedy_rising_volume(code):
                buy_list.append(code)

        # 급등리스트 파일에 쓴다
        self.st_mod01.update_buy_list(buy_list)

        # self.st_mod01.reset_data_opw00018()
        # account_number = self.mi_mod02.get_login_info("ACCNO")
        # print(account_number)
        # account_number = account_number.split(';')[0]
        # print(account_number)
        #
        # self.mi_mod02.set_input_value("계좌번호", account_number)
        # self.mi_mod02.comm_rq_data("opw00018_req", "opw00018", 0, "2000")
        # print(self.mi_mod02.opw00018_output['single'])
        # print(self.mi_mod02.opw00018_output['multi'])

if __name__ == "__main__":
    print("__main__")
    app = QApplication(sys.argv)
    ats = ATS()
    ats.run()
