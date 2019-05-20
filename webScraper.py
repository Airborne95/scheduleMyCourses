#!/usr/bin/python
from lxml import html
import requests
import webbrowser

# Open text file
def openFile(filename):
	try:
		fileObject = open(filename,'r+',0)
	except:
		fileObject = open(filename,'w')
	return fileObject

# Close text file
def closeFile(fileObject):
	fileObject.close()

# Empty a file
def emptyFile(filename):
	fileObject = open(filename, 'w').close()

# Read a file
def readFile(fileObject):
	for line in fileObject:
		print(line.rstrip("\n"))

def createSengCourseURL(courseNumber):
	url = "https://web.uvic.ca/calendar2019-05/CDs/SENG/"+courseNumber+".html"
	webbrowser.open(url)


# TODO add a proper description
def initialScrape(fileObject,filename):
	page = requests.get('https://web.uvic.ca/calendar2019-05/CDs/SENG/CTs.html')
	tree = html.fromstring(page.content)

	courseNumbers = tree.xpath('//td[1]/a/text()')
	courseTitles = tree.xpath('//td[last()]/a/text()')

	emptyFile(filename)
	for num,title in zip(courseNumbers,courseTitles):
		course = num+' '+title+'\n'
		fileObject.write(course)
	# print 'Seng Course Numbers: ', courseNumbers, '\n'
	# print 'Seng Course Titles: ', courseTitles

if __name__ == '__main__':
	filename = "dataSave.txt"
	fileObject = openFile(filename)
	# initialScrape(fileObject,filename)
	# closeFile(fileObject)
	readFile(fileObject)
	# createSengCourseURL('265')
