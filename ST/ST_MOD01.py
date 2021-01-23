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
        self.tr_kw_opt00081 = TR_KW_OPT10081.TR_KW_OPT10081(self.mi_mod02)
        self.tr_kw_opw00018 = TR_KW_OPW00018.TR_KW_OPW00018(self.mi_mod02)

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
        df = self.tr_kw_opt00081.tran_opt10081(code, today)
        print(self.tr_kw_opt10081.data_opt10081)
        volumes = df['volume']

        if len(volumes) < 21:
            return False

        sum_vol20 = 0
        today_vol = 0

        print (volumes)

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
