#!/usr/bin/python
from lxml import html
import requests
import webbrowser
import re
import datetime

# Open text file
def openFile(filename):
	# Try opening a file to read and write to it
	try:
		fileObject = open(filename,'r+',0)
	# If the file doesnt exist, create it and write to it.
	except:
		fileObject = open(filename,'w')
	# Return the file opened.
	return fileObject

# Close text file
def closeFile(fileObject):
	fileObject.close()

# Empty a text file
def emptyFile(filename):
	fileObject = open(filename, 'w').close()

# Read a text file
def readFile(fileObject):
	# For every line in fileObject = 'sengCourseNumbers.txt' currently
	for line in fileObject:
		# Take the number and remove the next line character
		for number in getCourseNumber(line.rstrip("\n")):
			# Get the appropriate link
			createSengCourseURL(number, fileObject)

def getCourseNumber(line):
	return re.findall(r'\d+\w+',line)

# Creates the link with the appropriate time stamp
def createSengCourseURL(courseNumber, fileObject):
	try:
		url = "https://web.uvic.ca/calendar"+getDate("new")+"/CDs/SENG/"+courseNumber+".html"
	except:
		url = "https://web.uvic.ca/calendar2019-05/CDs/SENG/"+courseNumber+".html"
	# scrapeTextFileName(url, fileObject)
	# webbrowser.open(url)


def getDate(flag):
	futureMonthDict = {1:"05",2:"05",3:"05",4:"05",5:"09",6:"09",7:"09",8:"09",9:"01",10:"01",11:"01",12:"01"}
	monthDict = {1:"01",2:"01",3:"01",4:"01",5:"05",6:"05",7:"05",8:"05",9:"09",10:"09",11:"09",12:"09"}
	# Variable to get today's date
	now = datetime.datetime.now()
	date=""
	if(flag.lower()=="new"):
		date = str(now.year)
		date = date+"-"+futureMonthDict[now.month]
	else:
		date= str(now.year)
		date = date+"-"+monthDict[now.month]
	print date
	# print str(now.month)
	# date = now.month + now.day
	# print  oldDate, date


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

def scrapeTextFileName(url, fileObject):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	courseNumber = tree.xpath('//h1/text()')
	# courseName = tree.xpath('//h2/text()')
	# for num, name in zip(courseNumber, courseName):
		# course = num + name
	for num in courseNumber:
		closeFile(openFile("textFiles/"+ num.replace(" ","")+".txt"))



if __name__ == '__main__':
	# fileSengCourseNumber = "textFiles/sengCourses.txt"
	# fileObject = openFile(fileSengCourseNumber)
	# initialScrape(fileObject,fileSengCourseNumber)
	# closeFile(fileObject)
	# fileObject = openFile(fileSengCourseNumber)
	# readFile(fileObject)
	getDate("old")
