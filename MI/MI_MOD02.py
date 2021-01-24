#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# 키움증권 공통모듈
#

import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import time
import pandas as pd
import sqlite3

from TR import TR_KW_OPT10081
from TR import TR_KW_OPW00018
from TR import TR_KW_OPW00001


class MI_MOD02(QAxWidget):
    def __init__(self):
        print("MI_MOD02__init__")
        super().__init__()

        # INIT 함수 호출
        self._create_mi_mod02_instance()  # 키움증권 Open API 인스턴스 생성
        self._set_signal_slots()  # PyQt5 콜백함수 셋팅

        # 공통변수 설정
        self.TR_REQ_TIME_INTERVAL = 0.5

        # TR모듈
        # self.tr_kw_opw00001 = TR_KW_opw00001.TR_KW_opw00001()
        self.tr_kw_opt10081 = TR_KW_OPT10081.TR_KW_OPT10081(self)
        self.tr_kw_opw00018 = TR_KW_OPW00018.TR_KW_OPW00018(self)
        self.tr_kw_opw00001 = TR_KW_OPW00001.TR_KW_OPW00001(self)

    def _create_mi_mod02_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._event_connect)  # 로그인처리
        self.OnReceiveTrData.connect(self._receive_tr_data)  # Transaction DATA 처리
        self.OnReceiveChejanData.connect(self._receive_chejan_data)  #

    # 로그인처리
    def comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        if err_code == 0:
            print("connected")
        else:
            print("disconnected")

        self.login_event_loop.exit()

    def get_code_list_by_market(self, market):
        code_list = self.dynamicCall("GetCodeListByMarket(QString)", market)
        code_list = code_list.split(';')
        return code_list[:-1]

    def get_master_code_name(self, code):
        code_name = self.dynamicCall("GetMasterCodeName(QString)", code)
        return code_name

    def get_connect_state(self):
        ret = self.dynamicCall("GetConnectState()")
        return ret

    def get_login_info(self, tag):
        ret = self.dynamicCall("GetLoginInfo(QString)", tag)
        return ret

    def set_input_value(self, id, value):
        self.dynamicCall("SetInputValue(QString, QString)", id, value)

    def comm_rq_data(self, rqname, trcode, next, screen_no):
        self.dynamicCall("CommRqData(QString, QString, int, QString)", rqname, trcode, next, screen_no)
        self.tr_event_loop = QEventLoop()
        self.tr_event_loop.exec_()

    def comm_get_data(self, code, real_type, field_name, index, item_name):
        # print("CommGetData("+code+", "+real_type+", "+field_name+", "+chr(index)+", "+item_name+")")
        ret = self.dynamicCall("CommGetData(QString, QString, QString, int, QString)", code,
                               real_type, field_name, index, item_name)
        # print(ret)
        return ret.strip()

    def get_repeat_cnt(self, trcode, rqname):
        print("GetRepeatCnt (" + trcode + ", " + rqname + ")")
        ret = self.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)
        print(ret)
        return ret

    def send_order(self, rqname, screen_no, acc_no, order_type, code, quantity, price, hoga, order_no):
        self.dynamicCall("SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                         [rqname, screen_no, acc_no, order_type, code, quantity, price, hoga, order_no])

    def get_chejan_data(self, fid):
        ret = self.dynamicCall("GetChejanData(int)", fid)
        return ret

    def get_server_gubun(self):
        ret = self.dynamicCall("KOA_Functions(QString, QString)", "GetServerGubun", "")
        return ret

    def _receive_tr_data(self, screen_no, rqname, trcode, record_name, next, unused1, unused2, unused3, unused4):
        print("_receive_tr_data start!! - rqname[" + rqname + "] trcode[" + trcode + "]")
        if next == '2':
            self.remained_data = True
        else:
            self.remained_data = False

        if rqname == "opt10081_req":
            self.tr_kw_opt10081.opt10081(rqname, trcode)
            # print(self.tr_kw_opt10081.data_opt10081)
        elif rqname == "opw00001_req":
            self.tr_kw_opw00001.opw00001(rqname, trcode)
        elif rqname == "opw00018_req":
            self.tr_kw_opw00018.opw00018(rqname, trcode)

        try:
            self.tr_event_loop.exit()
        except AttributeError:
            pass

    def _receive_chejan_data(self, gubun, item_cnt, fid_list):
        print(gubun)
        print(self.get_chejan_data(9203))
        print(self.get_chejan_data(302))
        print(self.get_chejan_data(900))
        print(self.get_chejan_data(901))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_mod02 = MI_MOD02()
    mi_mod02.comm_connect()

    mi_mod02.reset_opw00018_output()
    account_number = mi_mod02.get_login_info("ACCNO")
    account_number = account_number.split(';')[0]

    mi_mod02.set_input_value("계좌번호", account_number)
    mi_mod02.comm_rq_data("opw00018_req", "opw00018", 0, "2000")
    print(mi_mod02.opw00018_output['single'])
    print(mi_mod02.opw00018_output['multi'])
