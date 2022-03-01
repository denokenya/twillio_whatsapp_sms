from twilio.rest import Client 
import os
from dotenv import load_dotenv

load_dotenv()


account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('MY_TWILIO_AUTH_TOKEN')
 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid=os.getenv('TWILIO_MESSAGING_SERVICE_SID') , 
                              body='Hello How are you Sir?',      
                              to=os.getenv('TWILIO_TO'), 
                          ) 
 
print(message.sid)