#Author: mhdsecurity
#Description: The python version of scammer flooder. Do it for POC
from twilio.rest import Client
import time
import random
account_sid = ""
auth_token = ""
numbers=['+85290000000']
NumToCall=''

def call(fromNumber):
	try:
		client = Client(account_sid, auth_token)
		call = client.calls.create(to=NumToCall,
	                           from_=numbers,
	                           record=True,
	                           url="")
		print "Started call to: "+NumToCall+", from: "+fromNumber
	except:
		print "error"

def main():
	global NumToCall
	print "Scammer Flooder python version 1.0"
	NumToCall= raw_input('Enter the number to flood (+852 MUST BE IN FRONT!):')
	count=1
	while 1:
		print "Starting Call Batch" + str(count)
		call(random.choice(numbers))
		time.sleep(1)
		count+=1


if __name__ == '__main__':
    main()