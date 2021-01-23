#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# TR_KW_OPW00001 모듈
#

import sys
from MI import MI_MOD02


class TR_KW_OPW00001:
    def __init__(self, mi_mod01):
        print("TR_KW_opw00001__init__")
        self.mi_mod01 = mi_mod01

    def opw00001(self, rqname, trcode):
        d2_deposit = self.mi_mod01.comm_get_data(trcode, "", rqname, 0, "d+2추정예수금")
        d2_deposit = self.MI_MOD01.change_format(d2_deposit)
