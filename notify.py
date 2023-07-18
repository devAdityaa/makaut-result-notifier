from twilio.rest import Client
from decouple import config

account_sid = config('authSid')
auth_token = config('authT')
client = Client(account_sid, auth_token)

def send():
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='ulala',
    to='whatsapp:+918337052899'
    )
    return "Send Successfully!"
send()
