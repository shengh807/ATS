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

from MI import MI_MOD01

from TR import TR_KW_OPT10081
from TR import TR_KW_opw00001


class MI_MOD02(QAxWidget):
    def __init__(self):
        print("MI_MOD02__init__")
        super().__init__()

        # INIT 함수 호출
        self._create_mi_mod01_instance()  # 키움증권 Open API 인스턴스 생성
        self._set_signal_slots()  # PyQt5 콜백함수 셋팅

        # 공통변수 설정
        self.TR_REQ_TIME_INTERVAL = 0.5

        # TR모듈
        # self.tr_kw_opw00001 = TR_KW_opw00001.TR_KW_opw00001()
        self.tr_kw_opt10081 = TR_KW_OPT10081.TR_KW_OPT10081(self)

    def _create_mi_mod01_instance(self):
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
        ret = self.dynamicCall("CommGetData(QString, QString, QString, int, QString)", code,
                               real_type, field_name, index, item_name)
        return ret.strip()

    def get_repeat_cnt(self, trcode, rqname):
        ret = self.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)
        print("get_repeat_cnt (" + trcode + "," + rqname + ") : " + ret)
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

    def _opw00018(self, rqname, trcode):
        # single data
        total_purchase_price = self._comm_get_data(trcode, "", rqname, 0, "총매입금액")
        total_eval_price = self._comm_get_data(trcode, "", rqname, 0, "총평가금액")
        total_eval_profit_loss_price = self._comm_get_data(trcode, "", rqname, 0, "총평가손익금액")
        total_earning_rate = self._comm_get_data(trcode, "", rqname, 0, "총수익률(%)")
        estimated_deposit = self._comm_get_data(trcode, "", rqname, 0, "추정예탁자산")

        self.opw00018_output['single'].append(self.MI_MOD01.change_format(total_purchase_price))
        self.opw00018_output['single'].append(self.MI_MOD01.change_format(total_eval_price))
        self.opw00018_output['single'].append(self.MI_MOD01.change_format(total_eval_profit_loss_price))

        total_earning_rate = self.MI_MOD01.change_format(total_earning_rate)

        if self.get_server_gubun():
            total_earning_rate = float(total_earning_rate) / 100
            total_earning_rate = str(total_earning_rate)

        self.opw00018_output['single'].append(total_earning_rate)

        self.opw00018_output['single'].append(self.MI_MOD01.change_format(estimated_deposit))

        # multi data
        rows = self._get_repeat_cnt(trcode, rqname)
        for i in range(rows):
            name = self._comm_get_data(trcode, "", rqname, i, "종목명")
            quantity = self._comm_get_data(trcode, "", rqname, i, "보유수량")
            purchase_price = self._comm_get_data(trcode, "", rqname, i, "매입가")
            current_price = self._comm_get_data(trcode, "", rqname, i, "현재가")
            eval_profit_loss_price = self._comm_get_data(trcode, "", rqname, i, "평가손익")
            earning_rate = self._comm_get_data(trcode, "", rqname, i, "수익률(%)")

            quantity = self.MI_MOD01.change_format(quantity)
            purchase_price = self.MI_MOD01.change_format(purchase_price)
            current_price = self.MI_MOD01.change_format(current_price)
            eval_profit_loss_price = self.MI_MOD01.change_format(eval_profit_loss_price)
            earning_rate = self.MI_MOD01.change_format2(earning_rate)

            self.opw00018_output['multi'].append([name, quantity, purchase_price, current_price, eval_profit_loss_price,
                                                  earning_rate])

    # def reset_opw00018_output(self):
    #     self.opw00018_output = {'single': [], 'multi': []}

    def _receive_tr_data(self, screen_no, rqname, trcode, record_name, next, unused1, unused2, unused3, unused4):
        print("_receive_tr_data start!! - rqname[" + rqname + "] trcode[" + trcode + "]")
        if next == '2':
            self.remained_data = True
        else:
            self.remained_data = False

        if rqname == "opt10081_req":
            self.tr_kw_opt10081.opt10081(rqname, trcode)
        elif rqname == "opw00001_req":
            self.tr_kw_opw00001.opw00001(rqname, trcode)
        elif rqname == "opw00018_req":
            self._opw00018(rqname, trcode)

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
    mi_mod01 = MI_MOD02()
    mi_mod01.comm_connect()

    mi_mod01.reset_opw00018_output()
    account_number = mi_mod01.get_login_info("ACCNO")
    account_number = account_number.split(';')[0]

    mi_mod01.set_input_value("계좌번호", account_number)
    mi_mod01.comm_rq_data("opw00018_req", "opw00018", 0, "2000")
    print(mi_mod01.opw00018_output['single'])
    print(mi_mod01.opw00018_output['multi'])
