import urllib
import re
from stemming.porter2 import stem
import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords

file = open("vb.txt", "w")
def stems(speech,link):
	keywords = ["rais","fund","invest","land","inhal","lead","pull","$"]
	for i in speech:
		keyword = stem(i)
		for j in keywords:
			if j == keyword:
				indx = link.rfind("\" title")
				href = link[2:indx]
				print href
				print>>file, href
				print>>file, "--------------------------------------------------------------------"
				print "---------------------------------------------------------------------------"
				

def pos(token,link):
	for speech in token:
		#print a[1]
		if speech[1] == "NNS" or speech[1] == "VBZ" or speech[1] == "VBG" :
			stems(speech,link)
			
		
def tokens(link):
	index = link.rfind(",")
	name = link[index:]
	text = word_tokenize(name)
	token = nltk.pos_tag(text)
	pos(token,link)


	
def scrap(count):
	count+=1
	print "Page",count
	file = urllib.urlopen("http://venturebeat.com/page/%s"%count)
	text = file.read()
	expression = '<h2 class="entry-title">[\s]*<a href="(.+?)>(.+?)</a>[\s]*</h2>'
	pattern = re.compile(expression)
	isder = re.findall(pattern,text)
	for link in isder:
		tokens(str(link))
	#print len(isder)
	if len(isder) > 0:
		scrap(count)
		

def main():
	scrap(0)	
	

main()
			

#print "Total number of pages",count