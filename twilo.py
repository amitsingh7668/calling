import os
from twilio.rest import Client
 
account = "AC44f1a4e884484165192432b4fed84465"
token = "14105d634dc76a3de4f2580f3016682b"
client = Client(account,token)

call = client.calls.create(

    to = "+919769844424",
    from_ = "+12028388815",
    url = "https://demo.twilio.com/docs/voice.xml"
)

print(call.sid)