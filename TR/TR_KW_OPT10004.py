#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# TR_KW_OPT10004 모듈
#
# /********************************************************************/
# /// ########## Open API 함수를 이용한 전문처리 C++용 샘플코드 예제입니다.
#
#  [ opt10004 : 주식호가요청 ]
#
#  1. Open API 조회 함수 입력값을 설정합니다.
# 	종목코드 = 전문 조회할 종목코드
# 	SetInputValue("종목코드"	,  "000060");
#
#
#  2. Open API 조회 함수를 호출해서 전문을 서버로 전송합니다.
# 	CommRqData( "RQName"	,  "opt10004"	,  "0"	,  "화면번호");
#
# /********************************************************************/

import sys
from MI import MI_MOD02
import time
from pandas import DataFrame
from MI import MI_MOD11


class TR_KW_OPT10004:
    def __init__(self, mi_mod02):
        print("TR_KW_OPT10004__init__")
        self.mi_mod02 = mi_mod02
        self.data_opt10004 = {
            'st_cd': [],
            'st_dt': [],
            'sell_10_ratio': [],
            'sell_10_remain': [],
            'sell_10_prefer_price': [],
            'sell_9_ratio': [],
            'sell_9_remain': [],
            'sell_9_prefer_price': [],
            'sell_8_ratio': [],
            'sell_8_remain': [],
            'sell_8_prefer_price': [],
            'sell_7_ratio': [],
            'sell_7_remain': [],
            'sell_7_prefer_price': [],
            'sell_6_ratio': [],
            'sell_6_remain': [],
            'sell_6_prefer_price': [],
            'sell_5_ratio': [],
            'sell_5_remain': [],
            'sell_5_prefer_price': [],
            'sell_4_ratio': [],
            'sell_4_remain': [],
            'sell_4_prefer_price': [],
            'sell_3_ratio': [],
            'sell_3_remain': [],
            'sell_3_prefer_price': [],
            'sell_2_ratio': [],
            'sell_2_remain': [],
            'sell_2_prefer_price': [],
            'sell_1_ratio': [],
            'sell_priority_remain': [],
            'sell_priority_prefer_price': [],
            'buy_priority_prefer_price': [],
            'buy_priority_remain': [],
            'buy_1_ratio': [],
            'buy_2_prefer_price': [],
            'buy_2_remain': [],
            'buy_2_ratio': [],
            'buy_3_prefer_price': [],
            'buy_3_remain': [],
            'buy_3_ratio': [],
            'buy_4_prefer_price': [],
            'buy_4_remain': [],
            'buy_4_ratio': [],
            'buy_5_prefer_price': [],
            'buy_5_remain': [],
            'buy_5_ratio': [],
            'buy_6_prefer_price': [],
            'buy_6_remain': [],
            'buy_6_ratio': [],
            'buy_7_prefer_price': [],
            'buy_7_remain': [],
            'buy_7_ratio': [],
            'buy_8_prefer_price': [],
            'buy_8_remain': [],
            'buy_8_ratio': [],
            'buy_9_prefer_price': [],
            'buy_9_remain': [],
            'buy_9_ratio': [],
            'buy_10_prefer_price': [],
            'buy_10_remain': [],
            'buy_10_ratio': [],
            'sell_total_remain_before_ratio': [],
            'sell_total_remain': [],
            'buy_total_remain': [],
            'buy_total_remain_before_ratio': [],
            'sell_out_time_remain_before_ratio': [],
            'sell_out_time_remain': [],
            'buy_out_time_remain': [],
            'buy_out_time_remain_before_ratio': []
        }
        self.st_cd = ""

    # opt10004 주식기본정보요청
    def tran_opt10004(self, st_cd):
        print("tran_opt10004")
        self.st_cd = st_cd
        # print(self.st_cd)

        self.mi_mod02.set_input_value("종목코드", st_cd)
        self.mi_mod02.comm_rq_data("opt10004_req", "opt10004", 0, "1002")
        time.sleep(self.mi_mod02.TR_REQ_TIME_INTERVAL)

        # print(self.data_opt10004)
        df = DataFrame(self.data_opt10004, columns=[
            'st_cd',
            'st_dt',
            'sell_10_ratio',
            'sell_10_remain',
            'sell_10_prefer_price',
            'sell_9_ratio',
            'sell_9_remain',
            'sell_9_prefer_price',
            'sell_8_ratio',
            'sell_8_remain',
            'sell_8_prefer_price',
            'sell_7_ratio',
            'sell_7_remain',
            'sell_7_prefer_price',
            'sell_6_ratio',
            'sell_6_remain',
            'sell_6_prefer_price',
            'sell_5_ratio',
            'sell_5_remain',
            'sell_5_prefer_price',
            'sell_4_ratio',
            'sell_4_remain',
            'sell_4_prefer_price',
            'sell_3_ratio',
            'sell_3_remain',
            'sell_3_prefer_price',
            'sell_2_ratio',
            'sell_2_remain',
            'sell_2_prefer_price',
            'sell_1_ratio',
            'sell_priority_remain',
            'sell_priority_prefer_price',
            'buy_priority_prefer_price',
            'buy_priority_remain',
            'buy_1_ratio',
            'buy_2_prefer_price',
            'buy_2_remain',
            'buy_2_ratio',
            'buy_3_prefer_price',
            'buy_3_remain',
            'buy_3_ratio',
            'buy_4_prefer_price',
            'buy_4_remain',
            'buy_4_ratio',
            'buy_5_prefer_price',
            'buy_5_remain',
            'buy_5_ratio',
            'buy_6_prefer_price',
            'buy_6_remain',
            'buy_6_ratio',
            'buy_7_prefer_price',
            'buy_7_remain',
            'buy_7_ratio',
            'buy_8_prefer_price',
            'buy_8_remain',
            'buy_8_ratio',
            'buy_9_prefer_price',
            'buy_9_remain',
            'buy_9_ratio',
            'buy_10_prefer_price',
            'buy_10_remain',
            'buy_10_ratio',
            'sell_total_remain_before_ratio',
            'sell_total_remain',
            'buy_total_remain',
            'buy_total_remain_before_ratio',
            'sell_out_time_remain_before_ratio',
            'sell_out_time_remain',
            'buy_out_time_remain',
            'buy_out_time_remain_before_ratio'
        ])
        print(df)
        self.insert_table_opt10004(df)

        return df

    # DB Insert
    def insert_table_opt10004(self, df):
        print("insert_table_opt10004")
        # print(df)

        df['st_cd'] = self.st_cd
        # print(df)
        df.set_index('st_cd', inplace=True)

        # print("df.loc['st_cd'] [" + df.loc['st_cd'] + "] table insert!!")
        mi_mod11 = MI_MOD11.MI_MOD11()
        mi_mod11.insert_data_table("st_tb_stock_level_price", df)

    # RESPONSE 데이터 처리
    def opt10004(self, rqname, trcode):
        print("opt10004 (" + trcode + ", " + rqname + ")")

        data_cnt = self.mi_mod02.get_repeat_cnt(trcode, rqname)
        # print(data_cnt)
        self.data_opt10004 = {
            'st_dt': [],
            'sell_10_ratio': [],
            'sell_10_remain': [],
            'sell_10_prefer_price': [],
            'sell_9_ratio': [],
            'sell_9_remain': [],
            'sell_9_prefer_price': [],
            'sell_8_ratio': [],
            'sell_8_remain': [],
            'sell_8_prefer_price': [],
            'sell_7_ratio': [],
            'sell_7_remain': [],
            'sell_7_prefer_price': [],
            'sell_6_ratio': [],
            'sell_6_remain': [],
            'sell_6_prefer_price': [],
            'sell_5_ratio': [],
            'sell_5_remain': [],
            'sell_5_prefer_price': [],
            'sell_4_ratio': [],
            'sell_4_remain': [],
            'sell_4_prefer_price': [],
            'sell_3_ratio': [],
            'sell_3_remain': [],
            'sell_3_prefer_price': [],
            'sell_2_ratio': [],
            'sell_2_remain': [],
            'sell_2_prefer_price': [],
            'sell_1_ratio': [],
            'sell_priority_remain': [],
            'sell_priority_prefer_price': [],
            'buy_priority_prefer_price': [],
            'buy_priority_remain': [],
            'buy_1_ratio': [],
            'buy_2_prefer_price': [],
            'buy_2_remain': [],
            'buy_2_ratio': [],
            'buy_3_prefer_price': [],
            'buy_3_remain': [],
            'buy_3_ratio': [],
            'buy_4_prefer_price': [],
            'buy_4_remain': [],
            'buy_4_ratio': [],
            'buy_5_prefer_price': [],
            'buy_5_remain': [],
            'buy_5_ratio': [],
            'buy_6_prefer_price': [],
            'buy_6_remain': [],
            'buy_6_ratio': [],
            'buy_7_prefer_price': [],
            'buy_7_remain': [],
            'buy_7_ratio': [],
            'buy_8_prefer_price': [],
            'buy_8_remain': [],
            'buy_8_ratio': [],
            'buy_9_prefer_price': [],
            'buy_9_remain': [],
            'buy_9_ratio': [],
            'buy_10_prefer_price': [],
            'buy_10_remain': [],
            'buy_10_ratio': [],
            'sell_total_remain_before_ratio': [],
            'sell_total_remain': [],
            'buy_total_remain': [],
            'buy_total_remain_before_ratio': [],
            'sell_out_time_remain_before_ratio': [],
            'sell_out_time_remain': [],
            'buy_out_time_remain': [],
            'buy_out_time_remain_before_ratio': []
        }

        for i in range(data_cnt):
            opt10004_st_dt = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "호가잔량기준시간")
            opt10004_sell_10_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도10차선잔량대비")
            opt10004_sell_10_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도10차선잔량")
            opt10004_sell_10_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도10차선호가")
            opt10004_sell_9_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도9차선잔량대비")
            opt10004_sell_9_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도9차선잔량")
            opt10004_sell_9_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도9차선호가")
            opt10004_sell_8_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도8차선잔량대비")
            opt10004_sell_8_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도8차선잔량")
            opt10004_sell_8_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도8차선호가")
            opt10004_sell_7_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도7차선잔량대비")
            opt10004_sell_7_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도7차선잔량")
            opt10004_sell_7_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도7차선호가")
            opt10004_sell_6_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도6차선잔량대비")
            opt10004_sell_6_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도6우선잔량")
            opt10004_sell_6_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도6차선호가")
            opt10004_sell_5_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도5차선잔량대비")
            opt10004_sell_5_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도5차선잔량")
            opt10004_sell_5_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도5차선호가")
            opt10004_sell_4_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도4차선잔량대비")
            opt10004_sell_4_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도4차선잔량")
            opt10004_sell_4_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도4차선호가")
            opt10004_sell_3_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도3차선잔량대비")
            opt10004_sell_3_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도3차선잔량")
            opt10004_sell_3_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도3차선호가")
            opt10004_sell_2_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도2차선잔량대비")
            opt10004_sell_2_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도2차선잔량")
            opt10004_sell_2_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도2차선호가")
            opt10004_sell_1_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도1차선잔량대비")
            opt10004_sell_priority_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도최우선잔량")
            opt10004_sell_priority_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매도최우선호가")
    
            opt10004_buy_priority_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수최우선호가")
            opt10004_buy_priority_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수최우선잔량")
            opt10004_buy_1_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수1차선잔량대비")
            opt10004_buy_2_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수2차선호가")
            opt10004_buy_2_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수2차선잔량")
            opt10004_buy_2_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수2차선잔량대비")
            opt10004_buy_3_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수3차선호가")
            opt10004_buy_3_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수3차선잔량")
            opt10004_buy_3_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수3차선잔량대비")
            opt10004_buy_4_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수4차선호가")
            opt10004_buy_4_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수4차선잔량")
            opt10004_buy_4_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수4차선잔량대비")
            opt10004_buy_5_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수5차선호가")
            opt10004_buy_5_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수5차선잔량")
            opt10004_buy_5_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수5차선잔량대비")
            opt10004_buy_6_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수6우선호가")
            opt10004_buy_6_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수6우선잔량")
            opt10004_buy_6_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수6차선잔량대비")
            opt10004_buy_7_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수7차선호가")
            opt10004_buy_7_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수7차선잔량")
            opt10004_buy_7_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수7차선잔량대비")
            opt10004_buy_8_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수8차선호가")
            opt10004_buy_8_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수8차선잔량")
            opt10004_buy_8_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수8차선잔량대비")
            opt10004_buy_9_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수9차선호가")
            opt10004_buy_9_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수9차선잔량")
            opt10004_buy_9_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수9차선잔량대비")
            opt10004_buy_10_prefer_price = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수10차선호가")
            opt10004_buy_10_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수10차선잔량")
            opt10004_buy_10_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "매수10차선잔량대비")
    
            opt10004_sell_total_remain_before_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "총매도잔량직전대비")
            opt10004_sell_total_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "총매도잔량")
            opt10004_buy_total_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "총매수잔량")
            opt10004_buy_total_remain_before_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "총매수잔량직전대비")
    
            opt10004_sell_out_time_remain_before_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "시간외매도잔량대비")
            opt10004_sell_out_time_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "시간외매도잔량")
            opt10004_buy_out_time_remain = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "시간외매수잔량")
            opt10004_buy_out_time_remain_before_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, i, "시간외매수잔량대비")

            self.data_opt10004['st_dt'].append(opt10004_st_dt)
            self.data_opt10004['sell_10_ratio'].append(opt10004_sell_10_ratio)
            self.data_opt10004['sell_10_remain'].append(opt10004_sell_10_remain)
            self.data_opt10004['sell_10_prefer_price'].append(opt10004_sell_10_prefer_price)
            self.data_opt10004['sell_9_ratio'].append(opt10004_sell_9_ratio)
            self.data_opt10004['sell_9_remain'].append(opt10004_sell_9_remain)
            self.data_opt10004['sell_9_prefer_price'].append(opt10004_sell_9_prefer_price)
            self.data_opt10004['sell_8_ratio'].append(opt10004_sell_8_ratio)
            self.data_opt10004['sell_8_remain'].append(opt10004_sell_8_remain)
            self.data_opt10004['sell_8_prefer_price'].append(opt10004_sell_8_prefer_price)
            self.data_opt10004['sell_7_ratio'].append(opt10004_sell_7_ratio)
            self.data_opt10004['sell_7_remain'].append(opt10004_sell_7_remain)
            self.data_opt10004['sell_7_prefer_price'].append(opt10004_sell_7_prefer_price)
            self.data_opt10004['sell_6_ratio'].append(opt10004_sell_6_ratio)
            self.data_opt10004['sell_6_remain'].append(opt10004_sell_6_remain)
            self.data_opt10004['sell_6_prefer_price'].append(opt10004_sell_6_prefer_price)
            self.data_opt10004['sell_5_ratio'].append(opt10004_sell_5_ratio)
            self.data_opt10004['sell_5_remain'].append(opt10004_sell_5_remain)
            self.data_opt10004['sell_5_prefer_price'].append(opt10004_sell_5_prefer_price)
            self.data_opt10004['sell_4_ratio'].append(opt10004_sell_4_ratio)
            self.data_opt10004['sell_4_remain'].append(opt10004_sell_4_remain)
            self.data_opt10004['sell_4_prefer_price'].append(opt10004_sell_4_prefer_price)
            self.data_opt10004['sell_3_ratio'].append(opt10004_sell_3_ratio)
            self.data_opt10004['sell_3_remain'].append(opt10004_sell_3_remain)
            self.data_opt10004['sell_3_prefer_price'].append(opt10004_sell_3_prefer_price)
            self.data_opt10004['sell_2_ratio'].append(opt10004_sell_2_ratio)
            self.data_opt10004['sell_2_remain'].append(opt10004_sell_2_remain)
            self.data_opt10004['sell_2_prefer_price'].append(opt10004_sell_2_prefer_price)
            self.data_opt10004['sell_1_ratio'].append(opt10004_sell_1_ratio)
            self.data_opt10004['sell_priority_remain'].append(opt10004_sell_priority_remain)
            self.data_opt10004['sell_priority_prefer_price'].append(opt10004_sell_priority_prefer_price)
            self.data_opt10004['buy_priority_prefer_price'].append(opt10004_buy_priority_prefer_price)
            self.data_opt10004['buy_priority_remain'].append(opt10004_buy_priority_remain)
            self.data_opt10004['buy_1_ratio'].append(opt10004_buy_1_ratio)
            self.data_opt10004['buy_2_prefer_price'].append(opt10004_buy_2_prefer_price)
            self.data_opt10004['buy_2_remain'].append(opt10004_buy_2_remain)
            self.data_opt10004['buy_2_ratio'].append(opt10004_buy_2_ratio)
            self.data_opt10004['buy_3_prefer_price'].append(opt10004_buy_3_prefer_price)
            self.data_opt10004['buy_3_remain'].append(opt10004_buy_3_remain)
            self.data_opt10004['buy_3_ratio'].append(opt10004_buy_3_ratio)
            self.data_opt10004['buy_4_prefer_price'].append(opt10004_buy_4_prefer_price)
            self.data_opt10004['buy_4_remain'].append(opt10004_buy_4_remain)
            self.data_opt10004['buy_4_ratio'].append(opt10004_buy_4_ratio)
            self.data_opt10004['buy_5_prefer_price'].append(opt10004_buy_5_prefer_price)
            self.data_opt10004['buy_5_remain'].append(opt10004_buy_5_remain)
            self.data_opt10004['buy_5_ratio'].append(opt10004_buy_5_ratio)
            self.data_opt10004['buy_6_prefer_price'].append(opt10004_buy_6_prefer_price)
            self.data_opt10004['buy_6_remain'].append(opt10004_buy_6_remain)
            self.data_opt10004['buy_6_ratio'].append(opt10004_buy_6_ratio)
            self.data_opt10004['buy_7_prefer_price'].append(opt10004_buy_7_prefer_price)
            self.data_opt10004['buy_7_remain'].append(opt10004_buy_7_remain)
            self.data_opt10004['buy_7_ratio'].append(opt10004_buy_7_ratio)
            self.data_opt10004['buy_8_prefer_price'].append(opt10004_buy_8_prefer_price)
            self.data_opt10004['buy_8_remain'].append(opt10004_buy_8_remain)
            self.data_opt10004['buy_8_ratio'].append(opt10004_buy_8_ratio)
            self.data_opt10004['buy_9_prefer_price'].append(opt10004_buy_9_prefer_price)
            self.data_opt10004['buy_9_remain'].append(opt10004_buy_9_remain)
            self.data_opt10004['buy_9_ratio'].append(opt10004_buy_9_ratio)
            self.data_opt10004['buy_10_prefer_price'].append(opt10004_buy_10_prefer_price)
            self.data_opt10004['buy_10_remain'].append(opt10004_buy_10_remain)
            self.data_opt10004['buy_10_ratio'].append(opt10004_buy_10_ratio)
            self.data_opt10004['sell_total_remain_before_ratio'].append(opt10004_sell_total_remain_before_ratio)
            self.data_opt10004['sell_total_remain'].append(opt10004_sell_total_remain)
            self.data_opt10004['buy_total_remain'].append(opt10004_buy_total_remain)
            self.data_opt10004['buy_total_remain_before_ratio'].append(opt10004_buy_total_remain_before_ratio)
            self.data_opt10004['sell_out_time_remain_before_ratio'].append(opt10004_sell_out_time_remain_before_ratio)
            self.data_opt10004['sell_out_time_remain'].append(opt10004_sell_out_time_remain)
            self.data_opt10004['buy_out_time_remain'].append(opt10004_buy_out_time_remain)
            self.data_opt10004['buy_out_time_remain_before_ratio'].append(opt10004_buy_out_time_remain_before_ratio)

