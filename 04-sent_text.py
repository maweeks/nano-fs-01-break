from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC267641869b15bc21014a23663fd9ff49"
auth_token  = "de6c9f1d79439f714d0b7979a4aa8f1b"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
	body="Wassup...",
    to="+44 7515772568",    # Replace with your phone number
    from_="+44 1613751697") # Replace with your Twilio number
print message.sid