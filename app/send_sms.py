from twilio.rest import TwilioRestClient
from credentials import *

client = TwilioRestClient(account_sid, auth_token)

my_msg = 'Your message'

message = client.messages.create(to=my_cell, from_=my_twilio,
				body=my_msg)
messageTwo = client.messages.create(to=my_cellTwo, from_=my_twilio,
                                body=my_msg)

