#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# TR_KW_opt00081 모듈
#

import sys
from MI import MI_MOD02
import time
from pandas import DataFrame


class TR_KW_OPT10081:
    def __init__(self, mi_mod02):
        print("TR_KW_opt00081__init__")
        self.mi_mod02 = mi_mod02

    def opt10081(self, rqname, trcode):
        print("opt10081")
        data_cnt = self.mi_mod02.get_repeat_cnt(trcode, rqname)

        for i in range(data_cnt):
            opt10081_date = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "일자")
            opt10081_open = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "시가")
            opt10081_high = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "고가")
            opt10081_low = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "저가")
            opt10081_close = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "현재가")
            opt10081_volume = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "거래량")

            self.mi_mod02.ohlcv['date'].append(opt10081_date)
            self.mi_mod02.ohlcv['open'].append(int(opt10081_open))
            self.mi_mod02.ohlcv['high'].append(int(opt10081_high))
            self.mi_mod02.ohlcv['low'].append(int(opt10081_low))
            self.mi_mod02.ohlcv['close'].append(int(opt10081_close))
            self.mi_mod02.ohlcv['volume'].append(int(opt10081_volume))


    # opt10081 주식일봉차트조회요청
    def get_ohlcv(self, code, start):
        print("get_ohlcv")
        self.mi_mod02.ohlcv = {'date': [], 'open': [], 'high': [], 'low': [], 'close': [], 'volume': []}

        self.mi_mod02.set_input_value("종목코드", code)
        self.mi_mod02.set_input_value("기준일자", start)
        self.mi_mod02.set_input_value("수정주가구분", 1)
        self.mi_mod02.comm_rq_data("opt10081_req", "opt10081", 0, "0101")
        time.sleep(self.mi_mod02.TR_REQ_TIME_INTERVAL)

        print(self.mi_mod02.ohlcv)
        df = DataFrame(self.mi_mod02.ohlcv, columns=['open', 'high', 'low', 'close', 'volume'],
                       index=self.mi_mod02.ohlcv['date'])
        print(df)
        return df
