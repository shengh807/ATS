#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# TR_KW_OPT10001 모듈
#
# /********************************************************************/
# /// ########## Open API 함수를 이용한 전문처리 C++용 샘플코드 예제입니다.
#
#  [ opt10001 : 주식기본정보요청 ]
#
#  1. Open API 조회 함수 입력값을 설정합니다.
# 	종목코드 = 전문 조회할 종목코드
# 	SetInputValue("종목코드"	,  "입력값 1");
#
#
#  2. Open API 조회 함수를 호출해서 전문을 서버로 전송합니다.
# 	CommRqData( "RQName"	,  "opt10001"	,  "0"	,  "화면번호");
#
# /********************************************************************/

import sys
from MI import MI_MOD02
import time
from pandas import DataFrame
from MI import MI_MOD11


class TR_KW_OPT10001:
    def __init__(self, mi_mod02):
        print("TR_KW_OPT10001__init__")
        self.mi_mod02 = mi_mod02
        self.data_opt10001 = {
            'st_cd': [],
            'co_nm': [],
            'month_stmt': [],
            'face_value': [],
            'st_capital': [],
            'listed_shares': [],
            'credit_ratio': [],
            'best_price_of_year': [],
            'lowest_price_of_year': [],
            'market_cap': [],
            'share_of_market_capital': [],
            'external_burnout_rate': [],
            'substitute_price': [],
            'st_per': [],
            'st_eps': [],
            'st_roe': [],
            'st_pbr': [],
            'st_ev': [],
            'st_bps': [],
            'total_revenue': [],
            'operating_profit': [],
            'net_income': [],
            'day_250_highest': [],
            'day_250_lowest': [],
            'open': [],
            'high': [],
            'low': [],
            'upper_limit_price': [],
            'lower_limit_price': [],
            'standard_price': [],
            'estimated_stmt_price': [],
            'estimated_stmt_quantity': [],
            'best_250_day': [],
            'best_250_ratio': [],
            'lowest_250_day': [],
            'lowest_250_ratio': [],
            'close': [],
            'contrast_symbol': [],
            'net_change': [],
            'the_rate_of_fluctuation': [],
            'volume': [],
            'compared_to_transaction': [],
            'par_value_unit': [],
            'outstanding_stock': [],
            'current_ratio': []
        }
        self.st_cd = ""

    # opt10001 주식기본정보요청
    def tran_opt10001(self, st_cd):
        # print("tran_opt10001")
        self.st_cd = st_cd
        # print(self.st_cd)

        self.mi_mod02.set_input_value("종목코드", st_cd)
        self.mi_mod02.comm_rq_data("opt10001_req", "opt10001", 0, "1002")
        time.sleep(self.mi_mod02.TR_REQ_TIME_INTERVAL)

        # print(self.data_opt10001)
        df = DataFrame(self.data_opt10001, columns=[
            'st_cd',
            'co_nm',
            'month_stmt',
            'face_value',
            'st_capital',
            'listed_shares',
            'credit_ratio',
            'best_price_of_year',
            'lowest_price_of_year',
            'market_cap',
            'share_of_market_capital',
            'external_burnout_rate',
            'substitute_price',
            'st_per',
            'st_eps',
            'st_roe',
            'st_pbr',
            'st_ev',
            'st_bps',
            'total_revenue',
            'operating_profit',
            'net_income',
            'day_250_highest',
            'day_250_lowest',
            'open',
            'high',
            'low',
            'upper_limit_price',
            'lower_limit_price',
            'standard_price',
            'estimated_stmt_price',
            'estimated_stmt_quantity',
            'best_250_day',
            'best_250_ratio',
            'lowest_250_day',
            'lowest_250_ratio',
            'close',
            'contrast_symbol',
            'net_change',
            'the_rate_of_fluctuation',
            'volume',
            'compared_to_transaction',
            'par_value_unit',
            'outstanding_stock',
            'current_ratio'
        ])
        # print(df)
        self.insert_table_opt10001(df)

        return df

    # DB Insert
    def insert_table_opt10001(self, df):
        # print("insert_table_opt10001")
        # print(df)

        st_cd = df['st_cd']
        df.set_index('st_cd', inplace=True)

        if st_cd[0] != '' and st_cd[0] != '0' and st_cd[0] > '099440':
            # print("df.loc['st_cd'] [" + df.loc['st_cd'] + "] table insert!!")
            mi_mod11 = MI_MOD11.MI_MOD11()
            mi_mod11.insert_data_table("st_tb_stock_basic_info", df)

    # RESPONSE 데이터 처리
    def opt10001(self, rqname, trcode):
        # print("opt10001 (" + trcode + ", " + rqname + ")")
        
        self.data_opt10001 = {
            'st_cd': [],
            'co_nm': [],
            'month_stmt': [],
            'face_value': [],
            'st_capital': [],
            'listed_shares': [],
            'credit_ratio': [],
            'best_price_of_year': [],
            'lowest_price_of_year': [],
            'market_cap': [],
            'share_of_market_capital': [],
            'external_burnout_rate': [],
            'substitute_price': [],
            'st_per': [],
            'st_eps': [],
            'st_roe': [],
            'st_pbr': [],
            'st_ev': [],
            'st_bps': [],
            'total_revenue': [],
            'operating_profit': [],
            'net_income': [],
            'day_250_highest': [],
            'day_250_lowest': [],
            'open': [],
            'high': [],
            'low': [],
            'upper_limit_price': [],
            'lower_limit_price': [],
            'standard_price': [],
            'estimated_stmt_price': [],
            'estimated_stmt_quantity': [],
            'best_250_day': [],
            'best_250_ratio': [],
            'lowest_250_day': [],
            'lowest_250_ratio': [],
            'close': [],
            'contrast_symbol': [],
            'net_change': [],
            'the_rate_of_fluctuation': [],
            'volume': [],
            'compared_to_transaction': [],
            'par_value_unit': [],
            'outstanding_stock': [],
            'current_ratio': []
        }

        opt10001_st_cd = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "종목코드")
        opt10001_co_nm = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "종목명")
        opt10001_month_stmt = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "결산월")
        opt10001_face_value = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "액면가")
        opt10001_st_capital = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "자본금")
        opt10001_listed_shares = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "상장주식")
        opt10001_credit_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "신용비율")
        opt10001_best_price_of_year = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "연중최고")
        opt10001_lowest_price_of_year = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "연중최저")
        opt10001_market_cap = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "시가총액")
        opt10001_share_of_market_capital = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "시가총액비중")
        opt10001_external_burnout_rate = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "외인소진률")
        opt10001_substitute_price = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "대용가")
        opt10001_st_per = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "PER")
        opt10001_st_eps = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "EPS")
        opt10001_st_roe = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "ROE")
        opt10001_st_pbr = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "PBR")
        opt10001_st_ev = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "EV")
        opt10001_st_bps = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "BPS")
        opt10001_total_revenue = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "매출액")
        opt10001_operating_profit = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "영업이익")
        opt10001_net_income = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "당기순이익")
        opt10001_day_250_highest = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "250최고")
        opt10001_day_250_lowest = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "250최저")
        opt10001_open = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "시가")
        opt10001_high = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "고가")
        opt10001_low = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "저가")
        opt10001_upper_limit_price = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "상한가")
        opt10001_lower_limit_price = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "하한가")
        opt10001_standard_price = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "기준가")
        opt10001_estimated_stmt_price = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "예상체결가")
        opt10001_estimated_stmt_quantity = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "예상체결수량")
        opt10001_best_250_day = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "250최고가일")
        opt10001_best_250_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "250최고가대비율")
        opt10001_lowest_250_day = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "250최저가일")
        opt10001_lowest_250_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "250최저가대비율")
        opt10001_close = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "현재가")
        opt10001_contrast_symbol = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "대비기호")
        opt10001_net_change = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "전일대비")
        opt10001_the_rate_of_fluctuation = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "등락율")
        opt10001_volume = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "거래량")
        opt10001_compared_to_transaction = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "거래대비")
        opt10001_par_value_unit = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "액면가단위")
        opt10001_outstanding_stock = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "유통주식")
        opt10001_current_ratio = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "유통비율")

        self.data_opt10001['st_cd'].append(opt10001_st_cd)
        self.data_opt10001['co_nm'].append(opt10001_co_nm)
        self.data_opt10001['month_stmt'].append(opt10001_month_stmt)
        self.data_opt10001['face_value'].append(opt10001_face_value)
        self.data_opt10001['st_capital'].append(opt10001_st_capital)
        self.data_opt10001['listed_shares'].append(opt10001_listed_shares)
        self.data_opt10001['credit_ratio'].append(opt10001_credit_ratio)
        self.data_opt10001['best_price_of_year'].append(opt10001_best_price_of_year)
        self.data_opt10001['lowest_price_of_year'].append(opt10001_lowest_price_of_year)
        self.data_opt10001['market_cap'].append(opt10001_market_cap)
        self.data_opt10001['share_of_market_capital'].append(opt10001_share_of_market_capital)
        self.data_opt10001['external_burnout_rate'].append(opt10001_external_burnout_rate)
        self.data_opt10001['substitute_price'].append(opt10001_substitute_price)
        self.data_opt10001['st_per'].append(opt10001_st_per)
        self.data_opt10001['st_eps'].append(opt10001_st_eps)
        self.data_opt10001['st_roe'].append(opt10001_st_roe)
        self.data_opt10001['st_pbr'].append(opt10001_st_pbr)
        self.data_opt10001['st_ev'].append(opt10001_st_ev)
        self.data_opt10001['st_bps'].append(opt10001_st_bps)
        self.data_opt10001['total_revenue'].append(opt10001_total_revenue)
        self.data_opt10001['operating_profit'].append(opt10001_operating_profit)
        self.data_opt10001['net_income'].append(opt10001_net_income)
        self.data_opt10001['day_250_highest'].append(opt10001_day_250_highest)
        self.data_opt10001['day_250_lowest'].append(opt10001_day_250_lowest)
        self.data_opt10001['open'].append(opt10001_open)
        self.data_opt10001['high'].append(opt10001_high)
        self.data_opt10001['low'].append(opt10001_low)
        self.data_opt10001['upper_limit_price'].append(opt10001_upper_limit_price)
        self.data_opt10001['lower_limit_price'].append(opt10001_lower_limit_price)
        self.data_opt10001['standard_price'].append(opt10001_standard_price)
        self.data_opt10001['estimated_stmt_price'].append(opt10001_estimated_stmt_price)
        self.data_opt10001['estimated_stmt_quantity'].append(opt10001_estimated_stmt_quantity)
        self.data_opt10001['best_250_day'].append(opt10001_best_250_day)
        self.data_opt10001['best_250_ratio'].append(opt10001_best_250_ratio)
        self.data_opt10001['lowest_250_day'].append(opt10001_lowest_250_day)
        self.data_opt10001['lowest_250_ratio'].append(opt10001_lowest_250_ratio)
        self.data_opt10001['close'].append(opt10001_close)
        self.data_opt10001['contrast_symbol'].append(opt10001_contrast_symbol)
        self.data_opt10001['net_change'].append(opt10001_net_change)
        self.data_opt10001['the_rate_of_fluctuation'].append(opt10001_the_rate_of_fluctuation)
        self.data_opt10001['volume'].append(opt10001_volume)
        self.data_opt10001['compared_to_transaction'].append(opt10001_compared_to_transaction)
        self.data_opt10001['par_value_unit'].append(opt10001_par_value_unit)
        self.data_opt10001['outstanding_stock'].append(opt10001_outstanding_stock)
        self.data_opt10001['current_ratio'].append(opt10001_current_ratio)

