#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# 키움증권 주식 관련 CLASS
#
import sys
from PyQt5.QtWidgets import *
from MI import MI_MOD02
import time
from pandas import DataFrame
import datetime

MARKET_KOSPI   = 0
MARKET_KOSDAQ  = 10

from TR import TR_KW_OPT10081
from TR import TR_KW_OPW00018

class ST_MOD01:
    def __init__(self, mi_mod02):
        print("ST_MOD01__init__")
        # 공통모듈
        self.mi_mod02 = mi_mod02
        self.tr_kw_opt10001 = self.mi_mod02.tr_kw_opt10001
        self.tr_kw_opt10004 = self.mi_mod02.tr_kw_opt10004
        self.tr_kw_opt10081 = self.mi_mod02.tr_kw_opt10081
        self.tr_kw_opw00018 = self.mi_mod02.tr_kw_opw00018
        self.tr_kw_opw00001 = self.mi_mod02.tr_kw_opw00001

    # 코스피, 코스닥 종목코드 가지고옴.
    def get_code_list(self):
        print("get_code_list")
        self.kospi_codes = self.mi_mod02.get_code_list_by_market(MARKET_KOSPI)
        self.kosdaq_codes = self.mi_mod02.get_code_list_by_market(MARKET_KOSDAQ)
        print("kospi_codes : ")
        print(self.kospi_codes)
        print(self.kosdaq_codes)


    # 급등주인지 확인한다
    def check_speedy_rising_volume(self, code):
        # print("check_speedy_rising_volume")
        today = datetime.datetime.today().strftime("%Y%m%d") # 20210118
        df = self.tr_kw_opt10081.tran_opt10081(code, today)
        print(self.tr_kw_opt10081.data_opt10081)

        volumes = df['volume']

        if len(volumes) < 21:
            return False

        sum_vol20 = 0
        today_vol = 0

        print(volumes)

        for i, vol in enumerate(volumes):
            if i == 0:
                today_vol = vol
            elif 1 <= i <= 20:
                sum_vol20 += vol
            else:
                break

        avg_vol20 = sum_vol20 / 20
        if today_vol > avg_vol20 * 10:
            return True

    def update_buy_list(self, buy_list):
        print("update_buy_list")
        f = open("buy_list.txt", "wt")
        for code in buy_list:
            f.writelines("매수;", code, ";시장가;10;0;매수전")
        f.close()

    def get_account_amount(self, accno):
        print("get_account_amount")

        df = self.tr_kw_opw00018.tran_opw00018(accno)

        # for account_number in account_number:
        #     df = self.tr_kw_opw00018.tran_opw00018(account_number)

    def get_yesugum_amount(self, accno):
        print("get_yesugum_amount")

        df = self.tr_kw_opw00001.tran_opw00001(accno)

    # 기업정보 조회
    def get_stock_info(self, st_cd):
        # print("get_stock_info")

        df = self.tr_kw_opt10001.tran_opt10001(st_cd)

    # 호가정보 조회
    def get_level_price_info(self, st_cd):
        # print("get_level_price_info")

        df = self.tr_kw_opt10004.tran_opt10004(st_cd)
