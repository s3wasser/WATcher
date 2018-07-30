from twilio.rest import Client

standardPhoneNumberSize = 10

class TextMessageManager:
	
	# SID and AuthToken from Twilio account. Supply your own to the class.
	# twilioPhoneNum should be passed in as a string
	def __init__(self, accountSID, accountAuthToken, twilioPhoneNum):
		self.client = Client(accountSID, accountAuthToken)
		self.twilioPhoneNum = twilioPhoneNum 

	# phone #s should be passed in as strings to avoid integer overflow
	# Note: from # must be a Twilio number
	def sendTextMessage(self, recipientPhoneNum, msgBody):
		
		# Adding '+1' to numbers if they are not already appended
		if (len(recipientPhoneNum) == standardPhoneNumberSize):
			recipientPhoneNum = '+1' + recipientPhoneNum
		
		if (len(self.twilioPhoneNum) == standardPhoneNumberSize):
			self.twilioPhoneNum = '+1' + self.twilioPhoneNum

		self.client.messages.create(to=recipientPhoneNum, 
                       				from_= self.twilioPhoneNum,
                       				body=msgBody)


	# Helpers
	def createCourseAvailableMsg(self, courseNum, courseSection, subject):
		courseAvailMsg = 'LEC 00' + str(courseSection) + ' of ' + subject + ' ' + str(courseNum)
		msgIntro = 'Hey UWaterloo Student! You\'re in luck!\n\n' + courseAvailMsg + ' is now available!\n \n'
		msgOutro = 'What are you waiting for!? Head on over to Quest now! Godspeed my little goosling!\n -Mr. Goose'
		finalMsg = msgIntro + msgOutro

		return finalMsg