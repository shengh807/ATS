#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# KRX 공통모듈
#

import pandas as pd
import pandas_datareader as pdr

stock_type = {
    'kospi': 'stockMkt',
    'kosdaq': 'kosdaqMkt'
}

class MI_MOD03:
    def __init__(self):
        print("MI_MOD03__init__")
        # 공통모듈


    # 종목 타입에 따라 download url이 다름. 종목코드 뒤에 .KS .KQ등이 입력되어야해서 Download Link 구분 필요


    # 회사명으로 주식 종목 코드를 획득할 수 있도록 하는 함수
    def get_code(self, df, name):
        code = df.query("name=='{}'".format(name))['code'].to_string(index=False)
        # 위와같이 code명을 가져오면 앞에 공백이 붙어있는 상황이 발생하여 앞뒤로 sript() 하여 공백 제거
        code = code.strip()
        return code

    # download url 조합
    @staticmethod
    def get_download_stock(market_type=None):
        market_type = stock_type[market_type]
        download_link = 'http://kind.krx.co.kr/corpgeneral/corpList.do'
        download_link = download_link + '?method=download'
        download_link = download_link + '&marketType=' + market_type
        df = pd.read_html(download_link, header=0)[0]
        return df

    # kospi 종목코드 목록 다운로드
    def get_download_kospi(self):
        df = MI_MOD03.get_download_stock('kospi')
        print(df)
        df.종목코드 = df.종목코드.map('{:06d}.KS'.format)
        df["종목구분"] = "KS"
        return df

    # kosdaq 종목코드 목록 다운로드
    def get_download_kosdaq(self):
        df = MI_MOD03.get_download_stock('kosdaq')
        print(df)
        df.종목코드 = df.종목코드.map('{:06d}.KQ'.format)
        df["종목구분"] = "KQ"
        return df

    def get_stock_infomation(self):
        # kospi, kosdaq 종목코드 각각 다운로드
        kospi_df = self.get_download_kospi()
        kosdaq_df = self.get_download_kosdaq()

        # data frame merge
        code_df = pd.concat([kospi_df, kosdaq_df])
        print(code_df)

        # data frame정리
        code_df = code_df[['회사명', '종목코드']]

        # data frame title 변경 '회사명' = name, 종목코드 = 'code'
        code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

        # 삼성전자의 종목코드 획득. data frame에는 이미 XXXXXX.KX 형태로 조합이 되어있음
        code = self.get_code(code_df, '삼성전자')

        # get_data_yahoo API를 통해서 yahho finance의 주식 종목 데이터를 가져온다.
        df = pdr.get_data_yahoo(code)
        print(df)
