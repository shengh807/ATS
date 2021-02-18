#
# 작성일 : 2021-02-02
# 작성자 : Daniel Nho
#
# /********************************************************************/
#
# /********************************************************************/

from TR import TR_KRX_CORP0001
from MI import MI_MOD11

class ATS_KRX_TEST:
    def __init__(self):
        print("__init__")

        # self.mi_mod03 = TR_KRX_CORP0001.TR_KRX_CORP0001()                 # 키움증권 공통모듈

        mi_mod11 = MI_MOD11.MI_MOD11()
        
        ##### INSERT 테스트
        # mi_mod11.insert_batch_data_table("st_tb_stock_info", df) # 최초 1회
        # mi_mod11.insert_batch_data_table("st_tb_stock_info", df)

        ##### SELECT 테스트
        df = mi_mod11.select_data_table("SELECT *  FROM st_tb_stock_info WHERE co_nm = '현대오토에버'");

        df.set_index('st_cd', inplace=True)
        mi_mod11.update_data_table("st_tb_stock_info", df) # 최초 1회


        # print(df)
        # print(df.info())

    def run(self):
        print("run!!")
        # df = self.mi_mod03.get_stock_infomation()
        # self.mi_mod03.get_stock_price(df, '삼성전자')


if __name__ == "__main__":
    print("__main__")
    ats = ATS_KRX_TEST()
    ats.run()


