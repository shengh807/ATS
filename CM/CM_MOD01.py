
#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# 고객모듈
#

import sys
from PyQt5.QtWidgets import *
import time
from pandas import DataFrame
import datetime


class CM_MOD01:
    def __init__(self, mi_mod02):
        print("CM_MOD01__init__")
        # 공통모듈
        self.mi_mod02 = mi_mod02

    def login(self):
        self.mi_mod02.comm_connect()  # 로그인

    def get_account_list(self):
        # print("get_account_list")
        result = self.mi_mod02.get_login_info("ACCNO")

        accno_list = result.split(';')
        accno_list.remove('')

        return accno_list