# Util for chikka api
import http.client
import uuid
import json
import requests


CLIENT_ID = "7db826ec46490c86a590a15f08d2414192beda27711a066be371da5b84e19373"
SECRET_ID ="924124160f5ce9aa69188ef2a472f4855f28fab9f7ca13bc60716d519f041305"
SHORTCODE = '292908885'
API_URL = 'https://post.chikka.com/smsapi/request'

headers = {
    'content-type': "application/json",
    'accept': "application/json"
    }
conn = http.client.HTTPSConnection("post.chikka.com")

def send_sms(dest_num, msg):
    trans_id = str(uuid.uuid4())[:32].replace('-','1')
    payload = {'message_type':'SEND',
                'mobile_number':dest_num,
                'shortcode':SHORTCODE,
                'message_id':trans_id,
                'message':msg,
                'client_id':CLIENT_ID,
                'secret_key':SECRET_ID
                }

    response = requests.post(API_URL, data=payload)
    return response.text


# test
# print send_sms('639172449967', "HOOYAH!!")
