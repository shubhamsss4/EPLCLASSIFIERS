#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
from bs4 import BeautifulSoup

import requests

#print 'Argument List:', str(sys.argv)
#listinp=str(sys.argv).split(",")
#url=str(listinp[1].rstrip("]"))
#url.rstrip("'")
#url.lstrip("'")
#print url
#UTD VS SWA
listofmatches=[]
#http://www.espn.in/football/report?gameId=450635
for i in range(451007,451008):

	url = 'http://www.espn.in/football/report?gameId='+str(i)
	#AFC VS WAL
	#url = 'http://www.espn.in/football/report?gameId=480894'
	#BUN VS WESTHAM
	#url = 'http://www.espn.in/football/report?gameId=480895'

	r = requests.get(url)
	soup = BeautifulSoup(r.text,"lxml")

	print("**********************************REPORT*************************************************************")
	titlecontent=soup.find_all("article",attrs={"class":"article"})
	try:
		dateofmatch=titlecontent[0].find_all("span",attrs={"data-dateformat":"date1"})
		print(dateofmatch[0].text)
	except:
		listofmatches.append(i)
		continue
	away_data=soup.find_all("div",{"class":"team-info"})
	team_away_abbrev=away_data[0].find_all("span",attrs={"class":"abbrev"})


	team_home_abbrev=away_data[1].find_all("span",attrs={"class":"abbrev"})


	filename=str(team_away_abbrev[0].text)+"vs"+str(team_home_abbrev[0].text)+":"+str(dateofmatch[0].text)+str(".txt")
	filename=filename.replace(" ", "")


	file = open(filename,"w") 

	team_away=away_data[0].find_all("span",attrs={"class":"long-name"})
	file.write(team_away[0].text)
	file.write(" VS ")



	team_home=away_data[1].find_all("span",attrs={"class":"long-name"})
	file.write(team_home[0].text)
	file.write("\n")	
		


	file.write(dateofmatch[0].text)
	file.write("\n")
	reportheading=titlecontent[0].find_all("h1")
	try:
		for title in reportheading:
			print(title.text)
			file.write(title.text) 
	except:
		pass
	file.write("\n\n")	
	print("------------------------------------------------------------------------------------------------------")


	reportcontent=soup.find_all("div",attrs={"class":"article-body"})
	textcontent=reportcontent[0].find_all("p")
	for paragraph in textcontent:
		print(paragraph.text)
		file.write((paragraph.text).encode('ascii', 'ignore').decode('ascii'))
		file.write("\n")
	print("*****************************************************************************************************")


	file.close()
