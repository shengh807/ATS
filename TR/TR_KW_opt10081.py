#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# TR_KW_opt00081 모듈
#

import sys
from MI import MI_MOD01


class TR_KW_opt00081:
    def __init__(self, mi_mod01):
        print("TR_KW_opt00081__init__")
        self.mi_mod01 = mi_mod01

    def opt10081(self, rqname, trcode):
        data_cnt = self.get_repeat_cnt(trcode, rqname)

        for i in range(data_cnt):
            opt10081_date = self.mi_mod01.comm_get_data(trcode, "", rqname, i, "일자")
            opt10081_open = self.mi_mod01.comm_get_data(trcode, "", rqname, i, "시가")
            opt10081_high = self.mi_mod01.comm_get_data(trcode, "", rqname, i, "고가")
            opt10081_low = self.mi_mod01.comm_get_data(trcode, "", rqname, i, "저가")
            opt10081_close = self.mi_mod01.comm_get_data(trcode, "", rqname, i, "현재가")
            opt10081_volume = self.mi_mod01.comm_get_data(trcode, "", rqname, i, "거래량")

            self.ohlcv['date'].append(opt10081_date)
            self.ohlcv['open'].append(int(opt10081_open))
            self.ohlcv['high'].append(int(opt10081_high))
            self.ohlcv['low'].append(int(opt10081_low))
            self.ohlcv['close'].append(int(opt10081_close))
            self.ohlcv['volume'].append(int(opt10081_volume))


