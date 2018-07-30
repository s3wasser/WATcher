from TableQueryHelpers import *
from HTMLScraper import *
from TextMessageManager import *
from Globals import *

# TODO: abstract to "isCourseAvailable" function that returns bool, create init to parse and update col headers, then call isCourseAvailable on
# each course the user requests. That is better design and will help simplify the logic in this function
def checkCourseAvailability(courseNum, subject, termSessionNumber, lectureSectionsDesired): # lectureSectionsDesired = array of sections. MUST be valid
	parser = HTMLTableParser(courseNum, subject, termSessionNumber)
	courseTable = parser.getCourseInformationTable()
	updateTableHeaderLocationsCols(courseTable) # updates global vars for column header

	textMsgManager = TextMessageManager(twilioAccountSID, twilioAuthToken, twilioPhoneNum)

	for section in lectureSectionsDesired:
		lectureRowNum = getLectureSectionRow(courseTable, section)

		#TODO: put into it's own function
		totalClassEnrolment = int((courseTable[lectureRowNum][Globals.totalEnrolmentCol]).strip())
		totalClassCapacity = int((courseTable[lectureRowNum][Globals.totalCapacityCol]).strip())

		if (totalClassEnrolment < totalClassCapacity):
			textMsgBody = textMsgManager.createCourseAvailableMsg(courseNum, section, subject)
			textMsgManager.sendTextMessage(userPhoneNum, textMsgBody)


