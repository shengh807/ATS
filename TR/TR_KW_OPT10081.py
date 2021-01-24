#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# TR_KW_OPT10081 모듈
#
# /********************************************************************/
# /// ########## Open API 함수를 이용한 전문처리 C++용 샘플코드 예제입니다.
#
#  [ opt10081 : 주식일봉차트조회요청 ]
#
#  [ 주의 ]
#  데이터 건수를 지정할 수 업고, 데이터 유무에따라 한번에 최대 600개가 조회됩니다.
#
#  1. Open API 조회 함수 입력값을 설정합니다.
# 	종목코드 = 전문 조회할 종목코드
# 	SetInputValue("종목코드"	,  "입력값 1");
#
# 	기준일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
# 	SetInputValue("기준일자"	,  "입력값 2");
#
# 	수정주가구분 = 0 or 1, 수신데이터 1:유상증자, 2:무상증자, 4:배당락, 8:액면분할, 16:액면병합, 32:기업합병, 64:감자, 256:권리락
# 	SetInputValue("수정주가구분"	,  "입력값 3");
#
#
#  2. Open API 조회 함수를 호출해서 전문을 서버로 전송합니다.
# 	CommRqData( "RQName"	,  "opt10081"	,  "0"	,  "화면번호");
#
# /********************************************************************/

import sys
from MI import MI_MOD02
import time
from pandas import DataFrame


class TR_KW_OPT10081:
    def __init__(self, mi_mod02):
        print("TR_KW_OPT10081__init__")
        self.mi_mod02 = mi_mod02
        self.data_opt10081 = {'date': [], 'open': [], 'high': [], 'low': [], 'close': [], 'volume': []}


    # opt10081 주식일봉차트조회요청
    def tran_opt10081(self, code, start):
        print("tran_opt10081")

        self.mi_mod02.set_input_value("종목코드", code)
        self.mi_mod02.set_input_value("기준일자", start)
        self.mi_mod02.set_input_value("수정주가구분", 1)
        self.mi_mod02.comm_rq_data("opt10081_req", "opt10081", 0, "0101")
        time.sleep(self.mi_mod02.TR_REQ_TIME_INTERVAL)

        # print(self.data_opt10081)
        df = DataFrame(self.data_opt10081, columns=['open', 'high', 'low', 'close', 'volume'],
                       index=self.data_opt10081['date'])
        # print(df)
        return df

    # RESPONSE 데이터 처리
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

            self.data_opt10081['date'].append(opt10081_date)
            self.data_opt10081['open'].append(int(opt10081_open))
            self.data_opt10081['high'].append(int(opt10081_high))
            self.data_opt10081['low'].append(int(opt10081_low))
            self.data_opt10081['close'].append(int(opt10081_close))
            self.data_opt10081['volume'].append(int(opt10081_volume))

