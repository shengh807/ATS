import sys
from PyQt5.QtWidgets import *
from MI import MI_MOD01
import time
from pandas import DataFrame
import datetime

MARKET_KOSPI   = 0
MARKET_KOSDAQ  = 10

class ST_MOD01:
    def __init__(self, mi_mod01):
        print("ST_MOD01__init__")
        # 공통모듈
        self.mi_mod01 = mi_mod01

    # 코스피, 코스닥 종목코드 가지고옴.
    def get_code_list(self):
        print("get_code_list")
        self.kospi_codes = self.mi_mod01.get_code_list_by_market(MARKET_KOSPI)
        self.kosdaq_codes = self.mi_mod01.get_code_list_by_market(MARKET_KOSDAQ)
        print("kospi_codes : ")
        print(self.kospi_codes)
        print(self.kosdaq_codes)

    # opt10081 주식일봉차트조회요청
    def get_ohlcv(self, code, start):
        # print("get_ohlcv")
        self.mi_mod01.ohlcv = {'date': [], 'open': [], 'high': [], 'low': [], 'close': [], 'volume': []}

        self.mi_mod01.set_input_value("종목코드", code)
        self.mi_mod01.set_input_value("기준일자", start)
        self.mi_mod01.set_input_value("수정주가구분", 1)
        self.mi_mod01.comm_rq_data("opt10081_req", "opt10081", 0, "0101")
        time.sleep(self.mi_mod01.TR_REQ_TIME_INTERVAL)

        print(self.mi_mod01.ohlcv)
        df = DataFrame(self.mi_mod01.ohlcv, columns=['open', 'high', 'low', 'close', 'volume'],
                       index=self.mi_mod01.ohlcv['date'])
        print(df)
        return df

    # 급등주인지 확인한다
    def check_speedy_rising_volume(self, code):
        # print("check_speedy_rising_volume")
        today = datetime.datetime.today().strftime("%Y%m%d") # 20210118
        df = self.get_ohlcv(code, today)
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
