import sys
from PyQt5.QtWidgets import *
from MI import MI_MOD01
import time
from pandas import DataFrame
import datetime
from MI import MI_MOD01


class CM_MOD01:
    def __init__(self, mi_mod01):
        print("CM_MOD01__init__")
        # 공통모듈
        self.mi_mod01 = mi_mod01

    def get_account_list(self):
        # print("get_account_list")
        account_num = self.mi_mod01.dynamicCall("GetLoginInfo(QString)", ["ACCNO"])

        return account_num