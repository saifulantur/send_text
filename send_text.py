from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC293d4365c4c86ad37b7093b96393b6e7"
# Your Auth Token from twilio.com/console
auth_token  = "83975e8d92ed1e8e096284d2f572f409"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="", #My Number
    from_="+17165433770",
    body="Hello from Python!")

print(message.sid)
