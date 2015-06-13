# encoding=utf8
import urllib2
from bs4 import BeautifulSoup
import requests
import re

url = 'https://en.wikipedia.org/wiki/Spotify'
file = urllib2.urlopen(url)
text = file.read()
soup= BeautifulSoup(text)
    
table = soup.find("table", attrs={"class":"infobox vcard"})
for row in table.findAll("tr"):
	cells_header=row.findAll("th")
	cells=row.findAll("td")
	for a in cells_header:
		print a.string,cells[0].find(text=True)
