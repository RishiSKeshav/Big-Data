from bs4 import BeautifulSoup
import urllib
import requests
import re
import json
import statistics
import pymongo
import math

from pymongo import MongoClient

yearArray=["2009","2010","2011","2012","2013","2014"]
sectors=['Mobile Technolgies','Healthcare','Finance','Energy','Software Technology','Media','Hardware Components','Networks','ecommerce','social media']
yearTotal=[]
percentage2009Array=[]
percentage2010Array=[]
percentage2011Array=[]
percentage2012Array=[]
percentage2013Array=[]
percentage2014Array=[]
percentage2015Array=[]

def readDataSectorWise(year,sector):
	
	connection = MongoClient('localhost',27017)
	db = connection.vc_database
	collection = db.vc_collection2
	
	#for year1 in yearArray:
		#print year1
		#data = db.vc_collection21.find({"year":year1})
	#for sec in sectors:
	total=0.0
	count=0
	for data in db.vc_collection2.find({"sector":sector}):
		if data['year']==year:
			temp=data['amount']
			temp=str(temp)
			if temp != "":
				#print temp
				#s.find('$')==-1
				if 'M' in temp or 'B' in temp or 'K' in temp or 'm' in temp or 'k' in temp or 'b' in temp: 
				#if temp.find("M")==-1 or temp.find("B")==-1:
					#index=temp.index('M'|'B')
					#print temp
					if '-' in temp:
						continue
					if ',' in temp or '+' in temp or '?' in temp or ')' in temp:
						amount=temp[1:-2]
					else:
						amount=temp[1:-1]
					if 'M' in temp or 'm' in temp:
						amt=float(amount)*1000
					elif 'B' in temp or 'b' in temp:
						amt=float(amount)*1000000
					else:
						amt=float(amount) 
					#print sector,amount
					count+=1
					total=total+amt
					#sum = sum + amount
				
		#		else:
		#			amount=temp[1:len(temp)]
		#			#print sector,amount
		#			#print amount
		#			amt=1000*float(amount)
		#			#print data['link']
		#		#	print type(amount)
		#			amount = str(amount)	
		#			#print amount
		#			count+=1
		#			#	print type(amount)						
		#			total = total+amt
			
		#print "sum:", total*0.001,"Millions"
		#print count
					
	return total,count


	
def percentage():
	i=0
	for year in yearArray:
		
		print "Percentage"
		print "Year:",year
		year = str(year)
		finalTotal=0.0
		#filename=year+".tsv"
		#print filename
		#file = open(filename, "w")
		#print>>file, "Sector\tAmount"
		for sector in sectors:
			
			total=readData(year,sector)
			if total[1]!=0:
				sectorTemp=sector
				#print sector+" "+str(total[0]/1000)
				#print "Total for the year "+str(yearTotal[i])
				totalTemp=total[0]/1000
				print "Percentage: "+sector + ": "+ str((totalTemp/yearTotal[i])*100)
				temp = sectorTemp.replace(' ', '') +"\t"+ str(total[0]/1000)
			#	print>>file, temp
				#print temp
			else:
				print sector,":0"
		i+=1	
		print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
	#return finalTotal


		
def fetchSectorwise():
	for sector in sectors:
		
		print "Sector:",sector
		#year = str(year)
		
		filename=sector.replace(' ', '')+".tsv"
		print filename
		file = open(filename, "w")
		print>>file, "Year\tAmount"
		for year in yearArray:
		
			total=readDataSectorWise(year,sector)
			if total[1]!=0:
				sectorTemp=sector
				temp = year +"\t"+ str(total[0]/1000)
				print>>file, temp
				print temp
			else:
				print year,":0"
			
		print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"


		
def main():
	fetchYearwise()
	fetchSectorwise()
	percentage2009()
	percentage2010()
	percentage2011()
	percentage2012()
	percentage2013()
	percentage2014()
	
	#print "percentage2009Array",percentage2009Array
	#print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
	#print "percentage2010Array",percentage2010Array
	#print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
	#print "percentage2011Array",percentage2011Array
	#print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
	#print "percentage2012Array",percentage2012Array
	#print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
	#print "percentage2013Array",percentage2013Array
	#print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
	#print "percentage2014Array",percentage2014Array
	#print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
	#print yearTotal
	totalInvestment=getTotalInvestment2015()
	print "Total investment for 2015 "+str(totalInvestment)
	
	getInvestmentSectors2015(totalInvestment)
	#print percentage2015Array
	
	
	
main()
