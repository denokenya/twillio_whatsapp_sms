from twilio.rest import Client 
import os
from dotenv import load_dotenv

load_dotenv()


account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('MY_TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


first_name = input("What is your first name ?\n")
message = client.messages.create( 
                              from_=os.getenv('TWILIO_WHATSAPP_FROM'),  
                              body=f"Hello {first_name.capitalize()} how are you doing today ?",      
                              to=os.getenv('TWILIO_WHATSAPP_TO') ,
                              
                          ) 
 
print(message.sid)
print(f" Hello ,{first_name.capitalize()} we have sent you a whatsapp message!")