import Globals

# Helpers ************************************************
def findTableColumnFromHeader(tableHeader, table):
	tableHeaderRow = table[0]

	for counter, header in enumerate(tableHeaderRow):
		if header == tableHeader:
			return counter

	return 0

# Updates global values to get correct table headers
def updateTableHeaderLocationsCols(table):
	Globals.totalEnrolmentCol = findTableColumnFromHeader(Globals.enrolmentTotalStr, table)
	Globals.totalCapacityCol = findTableColumnFromHeader(Globals.enrolmentCapacityStr, table)
	Globals.lectureSectionCol = findTableColumnFromHeader(Globals.lectureSectionStr, table)

def getLectureSectionRow(table, lectureNumber): # lecture number should provided as an int (i.e. LEC 001 corresponds to lectureNumber = 1)
	for counter, courseRow in enumerate(table):
		if (courseRow[Globals.lectureSectionCol] == 'LEC 00' + str(lectureNumber) + ' '):
			return counter

	return 0