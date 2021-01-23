#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# TR_KW_OPW00018 모듈
#

import sys
from MI import MI_MOD02
import time
from pandas import DataFrame


class TR_KW_OPW00018:
    def __init__(self, mi_mod02):
        print("TR_KW_OPW00018__init__")
        self.mi_mod02 = mi_mod02


    def opw00018(self, rqname, trcode):
        print("opw00018")
        # single data
        total_purchase_price = self.mi_mod02._comm_get_data(trcode, "", rqname, 0, "총매입금액")
        total_eval_price = self.mi_mod02._comm_get_data(trcode, "", rqname, 0, "총평가금액")
        total_eval_profit_loss_price = self.mi_mod02._comm_get_data(trcode, "", rqname, 0, "총평가손익금액")
        total_earning_rate = self.mi_mod02._comm_get_data(trcode, "", rqname, 0, "총수익률(%)")
        estimated_deposit = self.mi_mod02._comm_get_data(trcode, "", rqname, 0, "추정예탁자산")

        self.mi_mod02.data_opw00018['single'].append(self.MI_MOD01.change_format(total_purchase_price))
        self.mi_mod02.data_opw00018['single'].append(self.MI_MOD01.change_format(total_eval_price))
        self.mi_mod02.data_opw00018['single'].append(self.MI_MOD01.change_format(total_eval_profit_loss_price))

        total_earning_rate = self.MI_MOD01.change_format(total_earning_rate)

        if self.mi_mod02.get_server_gubun():
            total_earning_rate = float(total_earning_rate) / 100
            total_earning_rate = str(total_earning_rate)

        self.mi_mod02.data_opw00018['single'].append(total_earning_rate)

        self.mi_mod02.data_opw00018['single'].append(self.MI_MOD01.change_format(estimated_deposit))

        # multi data
        rows = self.mi_mod02.get_repeat_cnt(trcode, rqname)
        for i in range(rows):
            name = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "종목명")
            quantity = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "보유수량")
            purchase_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매입가")
            current_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "현재가")
            eval_profit_loss_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "평가손익")
            earning_rate = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "수익률(%)")

            quantity = self.MI_MOD01.change_format(quantity)
            purchase_price = self.MI_MOD01.change_format(purchase_price)
            current_price = self.MI_MOD01.change_format(current_price)
            eval_profit_loss_price = self.MI_MOD01.change_format(eval_profit_loss_price)
            earning_rate = self.MI_MOD01.change_format2(earning_rate)

            self.mi_mod02.data_opw00018['multi'].append([name, quantity, purchase_price, current_price, eval_profit_loss_price,
                                                  earning_rate])

    def reset_data_opw00018(self):
        self.mi_mod02.data_opw00018 = {'single': [], 'multi': []}

    # OPW00081 주식일봉차트조회요청
    def tran_OPW00081(self, code, start):
        print("tran_OPW00081")
        self.mi_mod02.data_OPW00081 = {'date': [], 'open': [], 'high': [], 'low': [], 'close': [], 'volume': []}

        self.mi_mod02.set_input_value("종목코드", code)
        self.mi_mod02.set_input_value("기준일자", start)
        self.mi_mod02.set_input_value("수정주가구분", 1)
        self.mi_mod02.comm_rq_data("OPW00081_req", "OPW00081", 0, "0101")
        time.sleep(self.mi_mod02.TR_REQ_TIME_INTERVAL)

        print(self.mi_mod02.data_OPW00081)
        df = DataFrame(self.mi_mod02.data_OPW00081, columns=['open', 'high', 'low', 'close', 'volume'],
                       index=self.mi_mod02.data_OPW00081['date'])
        print(df)
        return df
