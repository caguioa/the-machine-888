# Util for UB api
import http.client
import uuid
import json


CLIENT_ID = "d956fccb-1867-4a3f-8b45-69da913e1da0"
SECRET_ID ="uN4dY0jM4uM8uU2qR0jD8wP3hA5gX4nY3iJ4tW0gN1mP2kS1vR"
conn = http.client.HTTPSConnection("api.us.apiconnect.ibmcloud.com")
headers = {
    'x-ibm-client-id': CLIENT_ID,
    'x-ibm-client-secret': SECRET_ID ,
    'content-type': "application/json",
    'accept': "application/json"
    }


# transfer funds api
'''
Response
{
  "channel_id": "BLUEMIX",
  "transaction_id": "1234567891",
  "status": "S",
  "confirmation_no": "T00000010175",
  "error_message": ""
}
'''

def transfer_funds(from_acct, to_acct, amount):
    trans_id = str(uuid.uuid4())
    payload = "{\"channel_id\":\"BLUEMIX\",\
                \"transaction_id\":\""+trans_id+"\",\
                \"source_account\":\""+ from_acct +"\",\
                \"source_currency\":\"php\",\
                \"target_account\":\""+to_acct+"\",\
                \"target_currency\":\"php\",\
                \"amount\":"+amount+"}"
    conn.request("POST", "/ubpapi-dev/sb/api/RESTs/transfer", payload, headers)
    res = conn.getresponse()
    data = res.read()
    ret = json.loads(data.decode("utf-8"))

    return ret

'''
Response
{
  "channel_id": "BLUEMIX",
  "transaction_id": "1234567891",
  "status": "S",
  "confirmation_no": "P00000000083",
  "error_message": ""
}
'''

def pay_bills(from_acct, biller_id, amount, ref1="", ref2="", ref3=""):
    trans_id = str(uuid.uuid4())
    conn = http.client.HTTPSConnection("api.us.apiconnect.ibmcloud.com")

    payload = "{\"channel_id\":\"BLUEMIX\",\
                \"transaction_id\":\""+trans_id+"\",\
                \"source_account\":\""+from_acct+"\",\
                \"source_currency\":\"php\",\
                \"biller_id\":\""+biller_id+"\",\
                \"reference1\":\""+ref1+"\",\
                \"reference2\":\""+ref2+"\",\
                \"reference3\":\""+ref3+"\",\
                \"amount\":"+amount+"}"
    conn.request("POST", "/ubpapi-dev/sb/api/RESTs/payment", payload, headers)

    res = conn.getresponse()
    data = res.read()
    ret = json.loads(data.decode("utf-8"))

    return ret

# account api
'''
Response
[
  {
    "account_no": "000000020000",
    "currency": "PHP",
    "account_name": "UBP 000000020000",
    "status": "Active",
    "available_balance": 92999,
    "current_balance": 92999
  }
]
'''
def get_account(account_no):
    conn.request("GET", "/ubpapi-dev/sb/api/RESTs/getAccount?account_no="+account_no, headers=headers)
    res = conn.getresponse()
    data = res.read()
    ret = json.loads(data.decode("utf-8"))[0]

    return ret
