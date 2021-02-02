#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# KRX 공통모듈
#

import pandas as pd
import pandas_datareader as pdr

from MI import MI_MOD11

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
        print(download_link)
        df = pd.read_html(download_link, header=0, converters={'종목코드': str})[0]
        print(df)
        return df

    # kospi 종목코드 목록 다운로드
    def get_download_kospi(self):
        df = MI_MOD03.get_download_stock('kospi')
        print(df)
        # df.종목코드 = df.종목코드.map('{:06d}.KS'.format)
        df["종목구분"] = "KS"
        return df

    # kosdaq 종목코드 목록 다운로드
    def get_download_kosdaq(self):
        df = MI_MOD03.get_download_stock('kosdaq')
        print(df)
        # df.종목코드 = df.종목코드.map('{:06d}.KQ'.format)
        df["종목구분"] = "KQ"
        return df

    def get_stock_infomation(self):
        # kospi, kosdaq 종목코드 각각 다운로드
        kospi_df = self.get_download_kospi()
        kosdaq_df = self.get_download_kosdaq()

        # data frame merge
        df = pd.concat([kospi_df, kosdaq_df])
        self.insert_stock_infomation(df)

        return df

    def insert_stock_infomation(self, df):
        df = df.rename(columns={'종목코드': 'st_cd', '종목구분': 'st_gubun', '회사명': 'co_nm', '업종': 'st_cn'
                                , '주요제품': 'item', '상장일': 'st_date', '결산월': 'pay_month', '대표자명': 'owner_nm'
                                , '홈페이지': 'homepage', '지역': 'region'})

        df.set_index('st_cd', inplace=True)
        df['st_date'''] = df['st_date'].str.replace('-', '')
        df['pay_month'] = df['pay_month'].str.replace('월', '')
        print(df)

        mi_mod11 = MI_MOD11.MI_MOD11()
        mi_mod11.insert_data_table("st_tb_stock_info", df)


    # get_data_yahoo 주식 가격정보 조회
    def get_stock_price(self, df, st_name):
        # data frame정리
        df['종목코드'] = df['종목코드'] + '.' + df['종목구분']
        df = df[['회사명', '종목코드']]

        # data frame title 변경 '회사명' = name, 종목코드 = 'code'
        df = df.rename(columns={'회사명': 'name', '종목코드': 'code'})

        # 삼성전자의 종목코드 획득. data frame에는 이미 XXXXXX.KX 형태로 조합이 되어있음
        code = self.get_code(df, st_name)

        # get_data_yahoo API를 통해서 yahho finance의 주식 종목 데이터를 가져온다.
        df = pdr.get_data_yahoo(code)
        print(df)

