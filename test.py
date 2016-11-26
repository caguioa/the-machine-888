import httplib
import json
CLIENT_ID = "d956fccb-1867-4a3f-8b45-69da913e1da0"
SECRET_ID ="uN4dY0jM4uM8uU2qR0jD8wP3hA5gX4nY3iJ4tW0gN1mP2kS1vR"


conn = http.client.HTTPSConnection("api.us.apiconnect.ibmcloud.com")


headers = {
      'x-ibm-client-id': CLIENT_ID,
      'x-ibm-client-secret': SECRET_ID,
      'content-type': "application/json",
      'accept': "application/json"
      }

conn.request("GET", "/ubpapi-dev/sb/api/RESTs/getAccount?account_no=101438806941", headers=headers)

res = conn.getresponse()
data = res.read()

ret = json.loads(data.decode("utf-8"))

print "Test account: %s :%s" %(ret[0]['account_name'], ret[0]['current_balance'])
