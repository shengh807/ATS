#
# 작성일 : 2021-02-02
# 작성자 : Daniel Nho
#
# /********************************************************************/
#
# /********************************************************************/

from MI import MI_MOD21

class ATS_KAKAO_TEST:

    def __init__(self):
        print("__init__")
        self.mi_mod21 = MI_MOD21.MI_MOD21()                 # 키움증권 공통모듈

    def run(self):
        print("run!!")
        return_code = self.mi_mod21.send_to_kakao("안녕하세요 테스트입니다")
        if return_code.status_code != "200":
            print(return_code.json())


if __name__ == "__main__":
    print("__main__")
    ats = ATS_KAKAO_TEST()
    ats.run()


