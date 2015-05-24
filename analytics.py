from bs4 import BeautifulSoup
import urllib
import requests
import re
import json
import statistics
import pymongo

from pymongo import MongoClient


#sector=dict()
yearArray=["2014","2015"]
sectors=['Mobile Technolgies','Healthcare','Finance','Energy','Software Technology','Media','Logistics','Hardware Components','Cloud platform','Networks','ecommerce','social media']

def sd():
	
	amountArray=[]

	connection = MongoClient('localhost',27017)
	db = connection.vc_database1
	collection = db.vc_collection1
	
	#for year1 in yearArray:
		#print year1
		#data = db.vc_collection1.find({"year":year1})
	#for sec in sectors:
	total=0.0
	count=0
	for year in yearArray:
		print "Standard Deviation"
		print "Year:",year
		for sector in sectors:
			for data in db.vc_collection1.find({"year":year,"sector":sector}):
				temp=data['amount']
				temp=str(temp)
				if temp != "":
					#print temp
					#s.find('$')==-1
					if 'M' in temp or 'B' in temp or 'K' in temp or 'm' in temp or 'k' in temp or 'b' in temp: 
					#if temp.find("M")==-1 or temp.find("B")==-1:
						#index=temp.index('M'|'B')
						amount=temp[1:-1]
						if 'M' in temp or 'm' in temp:
							amt=1000*float(amount)
							amountArray.append(amt)
						elif 'B' in temp or 'b' in temp:
							amt=1000000*float(amount)
							amountArray.append(amt)
						else:
							amt=float(amount) 
							amountArray.append(amt)
			print sector," : ",statistics.stdev(amountArray)
		print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"


def median():
	
	amount=[]
	
	connection = MongoClient('localhost',27017)
	db = connection.vc_database1
	collection = db.vc_collection1
	
	for year in yearArray:
		print "Median"
		print "Year:",year
		for sector in sectors:
			for data in db.vc_collection1.find({"year":year,"sector":sector}):
				temp=str(data['amount'])
				if temp != "":
					if 'M' in temp or 'B' in temp or 'K' in temp or 'm' in temp or 'k' in temp or 'b' in temp:
						amt=temp[1:-1]
						amount.append(float(amt))
					else:
						amt=temp[1:len(temp)]	
						amount.append(float(amt))
	
		print "median",statistics.median(amount)
		print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
		
		
	
	
def mean():
	
	for year in yearArray:
		print "Mean"
		print "Year:",year
		for sector in sectors:
			total=readData(year,sector)
			if total[1]!=0:
				print sector,":",total[0]/total[1]
			else:
				print sector,":0"
		print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"

def mode():

	amount=[]
	
	connection = MongoClient('localhost',27017)
	db = connection.vc_database1
	collection = db.vc_collection1
	
	for year in yearArray:
		for sector in sectors:
			for data in db.vc_collection1.find({"year":year,"sector":sector}):
				temp=str(data['amount'])
				if temp != "":
					amount.append((temp))
			if len(amount)>0:		
				print "mode for year", year,"sector",sector,"is",statistics.mode(amount)
			else:
				print "mode for year", year,"sector",sector,"is 	
def readData(year,sector):
	
	connection = MongoClient('localhost',27017)
	db = connection.vc_database1
	collection = db.vc_collection1
	
	#for year1 in yearArray:
		#print year1
		#data = db.vc_collection1.find({"year":year1})
	#for sec in sectors:
	total=0.0
	count=0
	for data in db.vc_collection1.find({"year":year}):
		if data['sector']==sector:
			temp=data['amount']
			temp=str(temp)
			if temp != "":
				#print temp
				#s.find('$')==-1
				if 'M' in temp or 'B' in temp or 'K' in temp or 'm' in temp or 'k' in temp or 'b' in temp: 
				#if temp.find("M")==-1 or temp.find("B")==-1:
					#index=temp.index('M'|'B')
					amount=temp[1:-1]
					if 'M' in temp or 'm' in temp:
						amt=float(amount)/1000
					elif 'B' in temp or 'b' in temp:
						amt=float(amount)/1000000
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
    
def main():
	mean()
	median()
	sd()
	mode()
	
main()
