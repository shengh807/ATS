#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# TR_KW_OPW00001 모듈
#
# /********************************************************************/
# /// ########## Open API 함수를 이용한 전문처리 C++용 샘플코드 예제입니다.
#
#  [ opw00001 : 예수금상세현황요청 ]
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
# 	조회구분 = 3:추정조회, 2:일반조회
# 	SetInputValue("조회구분"	,  "입력값 4");
#
#
#  2. Open API 조회 함수를 호출해서 전문을 서버로 전송합니다.
# 	CommRqData( "RQName"	,  "opw00001"	,  "0"	,  "화면번호");
#
# /********************************************************************/

import sys
from MI import MI_MOD01
import time


class TR_KW_OPW00001:
    def __init__(self, mi_mod02):
        print("TR_KW_OPW00001__init__")
        self.mi_mod02 = mi_mod02
        self.data_opw00001 = 0

    # OPW00018 계좌평가잔고내역요청
    def tran_opw00001(self, accno):
        print("tran_OPW00018")

        self.mi_mod02.set_input_value("계좌번호", accno)
        self.mi_mod02.set_input_value("비밀번호", "0320")
        self.mi_mod02.set_input_value("비밀번호입력매체구분", "00")
        self.mi_mod02.set_input_value("조회구분", "1");

        self.mi_mod02.comm_rq_data("opw00001_req", "opw00001", 0, "3000")
        time.sleep(self.mi_mod02.TR_REQ_TIME_INTERVAL)

        print(self.data_opw00001)

    # RESPONSE 데이터 처리
    def opw00001(self, rqname, trcode):
        opw00001_d2_deposit = self.mi_mod02.comm_get_data(trcode, "", rqname, 0, "d+2추정예수금")

        self.data_opw00001 = MI_MOD01.StringUtils.change_format(opw00001_d2_deposit)


