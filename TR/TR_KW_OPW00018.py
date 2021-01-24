#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# TR_KW_OPW00018 모듈
#
# /********************************************************************/
# /// ########## Open API 함수를 이용한 전문처리 C++용 샘플코드 예제입니다.
#
#  [ opw00018 : 계좌평가잔고내역요청 ]
#
#  [ 주의 ]
#  "수익률%" 데이터는 모의투자에서는 소숫점표현, 실거래서버에서는 소숫점으로 변환 필요 합니다.
#
#  1. Open API 조회 함수 입력값을 설정합니다.
# 	계좌번호 = 전문 조회할 보유계좌번호
# 	SetInputValue("계좌번호"	,  "입력값 1");
#
# 	비밀번호 = 사용안함(공백)
# 	SetInputValue("비밀번호"	,  "입력값 2");
#
# 	비밀번호입력매체구분 = 00
# 	SetInputValue("비밀번호입력매체구분"	,  "입력값 3");
#
# 	조회구분 = 1:합산, 2:개별
# 	SetInputValue("조회구분"	,  "입력값 4");
#
#
#  2. Open API 조회 함수를 호출해서 전문을 서버로 전송합니다.
# 	CommRqData( "RQName"	,  "opw00018"	,  "0"	,  "화면번호");
#
# /********************************************************************/


import sys
from MI import MI_MOD02
import time
from pandas import DataFrame

from MI import MI_MOD01


class TR_KW_OPW00018:
    def __init__(self, mi_mod02):
        print("TR_KW_OPW00018__init__")
        self.mi_mod02 = mi_mod02
        self.data_opw00018 = {'single': [], 'multi': []}

    def opw00018(self, rqname, trcode):
        print("opw00018")
        # single data
        opw00018_total_purchase_price = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "총매입금액")
        opw00018_total_eval_price = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "총평가금액")
        opw00018_total_eval_profit_loss_price = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "총평가손익금액")
        opw00018_total_earning_rate = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "총수익률(%)")
        opw00018_estimated_deposit = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "추정예탁자산")

        self.data_opw00018['single'].append(MI_MOD01.StringUtils.change_format(opw00018_total_purchase_price))
        self.data_opw00018['single'].append(MI_MOD01.StringUtils.change_format(opw00018_total_eval_price))
        self.data_opw00018['single'].append(MI_MOD01.StringUtils.change_format(opw00018_total_eval_profit_loss_price))

        total_earning_rate = MI_MOD01.StringUtils.change_format(opw00018_total_earning_rate)

        if self.mi_mod02.get_server_gubun():
            total_earning_rate = float(total_earning_rate) / 100
            total_earning_rate = str(total_earning_rate)

        self.data_opw00018['single'].append(total_earning_rate)

        self.data_opw00018['single'].append(MI_MOD01.StringUtils.change_format(opw00018_estimated_deposit))

        # multi data
        rows = self.mi_mod02.get_repeat_cnt(trcode, rqname)
        for i in range(rows):
            name = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "종목명")
            quantity = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "보유수량")
            purchase_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매입가")
            current_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "현재가")
            eval_profit_loss_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "평가손익")
            earning_rate = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "수익률(%)")

            quantity = MI_MOD01.StringUtils.change_format(quantity)
            purchase_price = MI_MOD01.StringUtils.change_format(purchase_price)
            current_price = MI_MOD01.StringUtils.change_format(current_price)
            eval_profit_loss_price = MI_MOD01.StringUtils.change_format(eval_profit_loss_price)
            earning_rate = MI_MOD01.StringUtils.change_format2(earning_rate)

            self.data_opw00018['multi'].append([name, quantity, purchase_price, current_price, eval_profit_loss_price,
                                                earning_rate])
            print(self.data_opw00018)

    def reset_data_opw00018(self):
        self.data_opw00018 = {'single': [], 'multi': []}


    # OPW00018 계좌평가잔고내역요청
    def tran_opw00018(self, account_number):
        print("tran_OPW00018")

        self.mi_mod02.set_input_value("계좌번호", account_number)
        self.mi_mod02.set_input_value("비밀번호", "0320")
        self.mi_mod02.comm_rq_data("opw00018_req", "opw00018", 0, "2000")
        print(self.mi_mod02.tr_kw_opw00018.data_opw00018['single'])
        print(self.mi_mod02.tr_kw_opw00018.data_opw00018['multi'])


        # self.mi_mod02.data_OPW00081 = {'date': [], 'open': [], 'high': [], 'low': [], 'close': [], 'volume': []}

        # self.mi_mod02.set_input_value("종목코드", code)
        # self.mi_mod02.set_input_value("기준일자", start)
        # self.mi_mod02.set_input_value("수정주가구분", 1)
        # self.mi_mod02.comm_rq_data("OPW00081_req", "OPW00081", 0, "0101")
        # time.sleep(self.mi_mod02.TR_REQ_TIME_INTERVAL)

        print(self.mi_mod02.data_OPW00081)
        df = DataFrame(self.mi_mod02.data_OPW00081, columns=['open', 'high', 'low', 'close', 'volume'],
                       index=self.mi_mod02.data_OPW00081['date'])
        print(df)
        return df
