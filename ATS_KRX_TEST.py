#
# 작성일 : 2021-02-02
# 작성자 : Daniel Nho
#
# /********************************************************************/
#
# /********************************************************************/

from MI import MI_MOD03


class ATS_KRX_TEST:
    def __init__(self):
        print("__init__")

        self.mi_mod03 = MI_MOD03.MI_MOD03()                 # 키움증권 공통모듈

    def run(self):
        print("run!!")
        df = self.mi_mod03.get_stock_infomation()
        self.mi_mod03.get_stock_price(df, '삼성전자')


if __name__ == "__main__":
    print("__main__")
    ats = ATS_KRX_TEST()
    ats.run()


