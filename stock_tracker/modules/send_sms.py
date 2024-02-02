## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

from twilio.rest import Client

def send_sms(body):
  account_sid = 'ENTER_ACCOUNT_SID'
  auth_token = 'ENTER_AUTH_TOKEN'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
    from_='+12564190572', #Enter twilio number for sending sms
    body=body,
    to='+919999999999' #Enter your number for receiving sms 
  )

  return message.sid