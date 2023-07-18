from twilio.rest import Client
from decouple import config

account_sid = 'AC6ae56368f1d6be131a3ac2a9e0db1bea'
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