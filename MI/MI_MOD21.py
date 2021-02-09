#
# 작성일 : 2021-01-18
# 작성자 : Daniel Nho
# 카카오톡 문자발송 공통모듈
#

# 1) 인가코드 받기
# https://kauth.kakao.com/oauth/authorize?client_id=a27443772de2a504f04950c1cee4fe5c&redirect_uri=https://dooho.shop&response_type=code
# https://dooho.shop/?code=bxy9eQAy5mqFPF0HppUPicE2JoPcQdfBMG15HHluCPbG5SxpOWEVwnlqPvDhfWnpBQlOVQopb9QAAAF3dTKtIw

# 2) 사용자 인증토큰 받기
# curl -v -X POST "https://kauth.kakao.com/oauth/token" \
#  -d "grant_type=authorization_code" \
#  -d "client_id=a27443772de2a504f04950c1cee4fe5c" \
#  -d "redirect_uri=https://dooho.shop" \
#  -d "code=j6paz9d2T9L2EM0JqDrhlSQ8OrcFsfSL_7Cun6f8seKyCvGix2Bi5rdlAzBFc5AntzWJNAo9dRsAAAF3dTnVWw"
#
# {"access_token":"6-cb2Sm5JEdpQle0ffTxwx5kmsHHSzrN7qQxRAo9dRkAAAF3dTo0Zg","token_type":"bearer","refresh_token":"NH6kQlCsRE6NiYiV7f7aQqc3fr_RBfgbctsVcwo9dRkAAAF3dTo0ZQ","expires_in":21599,"scope":"age_range birthday account_email talk_mes


import requests
import json

KAKAO_TOKEN = "6-cb2Sm5JEdpQle0ffTxwx5kmsHHSzrN7qQxRAo9dRkAAAF3dTo0Zg"

class MI_MOD21:
    def __init__(self):
        print("__init__")

    #카카오톡 메시지 전송
    def send_to_kakao(self, text):
        print("send_to_kakao : {}".format(text))


        header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}
        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        post = {
            "object_type": "text",
            "text": text,
            "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com"
            },
        }

        data = {"template_object": json.dumps(post)}

        return requests.post(url, data=data, headers=header)


# def send_to_kakao_friend(text):
#     print("send_to_kakao_friend : {}".format(text))

#     header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}
#     url = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
#     post = {
#         "object_type": "text",
#         "text": text,
#         "link": {
#             "web_url": "https://developers.kakao.com",
#             "mobile_web_url": "https://developers.kakao.com"
#         },
#     }

#     data = {"template_object": json.dumps(post)}

#     return requests.post(url, data=data, headers=header)


