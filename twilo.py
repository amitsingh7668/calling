import os
from twilio.rest import Client
 
account = ""
token = ""
client = Client(account,token)

call = client.calls.create(

    to = "+",
    from_ = "+",
    url = "https://demo.twilio.com/docs/voice.xml"
)

print(call.sid)
