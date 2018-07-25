import urllib2
from bs4 import BeautifulSoup

class HTMLTableParser:
	userAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
	headers = {'User-Agent': userAgent}

	def __init__(self, courseNum, subject, termSessionNumber):
		self.courseNum = courseNum
		self.subject = subject
		self.termSessionNumber = termSessionNumber

		baseUrl = 'http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?'
		self.requestUrl = baseUrl + 'sess=' + str(termSessionNumber) + '&subject=' + subject + '&cournum=' + str(courseNum)

	# html request to make soup, which returns the HTML webpage format
	def getHTMLFromPage(self):
		try:
			req = urllib2.Request(self.requestUrl, headers=self.headers)
			response = urllib2.urlopen(req)
		except urllib2.HTTPError, err:
			return -1
		else:
			html = response.read()
			soup = BeautifulSoup(html, 'html.parser')
			return soup

	# The first table on the site always seems to be generalized info about
	# the course itself that we don't need. Second table contains all the 
	# enrollment + course section stuff we need, so we'll return that.
	# Not the safest implementation, but this site is old and hasn't changed
	# in YEARS, so I'm willing to risk it

	def getCourseInfoTable(self, soup):
		return soup.findAll('table')[1] 

	def convertTableTo2DArray(self, table):
		result = []
		tableHeader = True
		allrows = table.findAll('tr')
		for row in allrows:
			result.append([])
			if (tableHeader):
				allcols = row.findAll('th') # the first row of the table is all table header tags, so we must differentiate between them
				tableHeader = False
			else:
				allcols = row.findAll('td')
			for col in allcols:
				thestrings = [unicode(s) for s in col.findAll(text=True)]
				thetext = ''.join(thestrings)
				result[-1].append(thetext)
		return result

	def getCourseInformationTable(self):
		soup = self.getHTMLFromPage()
		courseInfoTable = self.getCourseInfoTable(soup)
		courseInfoArray = self.convertTableTo2DArray(courseInfoTable)
		return courseInfoArray

