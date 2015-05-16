from bs4 import BeautifulSoup
import urllib
import requests
import json

sectorDictionary = dict()
sectorDictionary['Mobile Technolgies'] = ['mobile communication','mobile software','mobile technologies','Mobile & Communications','Mobile','mobile computing'
                                    ,'mobile services','mobile and wireless','wireless technology','media and telecoms','Early stage mobile','Mobile Services & Infrastructure']

sectorDictionary['Healthcare'] = ['healthcare Technology','Healthcare & Cleantech','Healthcare','Clean Tech','Technology and Healthcare','Digital Health'
                                    ,'Clean Technology','bio-tech','Life Sciences','Pharmaceuticals','Medical Technology','Biotechnology'
                            ,'BioMedicine','technology & Life Sciences','Medical','Biomedical Devices and New Drugs','Medical Devices','Specialty Pharmaceuticals'
                            ,'Wellness']

sectorDictionary['Finance'] = ['Business & Financial services','Business Services','Financial & Information Services','Real Estate']

sectorDictionary['Energy'] = ['Industrials & Energy','energy','Energy Technologies','Energy and Information Technology'
                        ,'Renewable Energy','Alternative energy','Energytech','Energy-Related Products and Services']

sectorDictionary['Software Technology'] = ['Information Services','IT Infrastructure','Enterprise Software','Infrastructure Software and Services'
                        ,'Software','Gaming','Software & Business Services','Software and Services','Applications']

sectorDictionary['Media'] = ['New Media','Internet','Interactive digital media','Internet and Digital Media'
                        ,'Media and Entertainment','Consumer Internet','Info and Comm Technology','Digital Home and Digital Media','advertising']

sectorDictionary['Logistics'] = ['maritime']

sectorDictionary['Hardware Components'] = ['Semiconductors and Components','Nanotechnology and Microsystems','Manufacturing and Memory','silicon technology'
                        ,'Hardware','Semiconductors']

sectorDictionary['Cloud platform'] = ['Cloud Computing','Cloud/SaaS','Cloud Services and Infrastructure']

sectorDictionary['Networks'] = ['Communications','Networking','Information and Communications Technology','Consumer and Business Networking Applications to networkingy']

sectorDictionary['ecommerce'] = ['Next-Gen Commerce','Internet-based Advertising','Web-Enabled Services']

sectorDictionary['social media'] = ['Social']

jsonList = []

def get_content(post_url):
    content=""
    r = requests.get(post_url)
    soup = BeautifulSoup(r.content)
    
    heading = soup.find("h1", "entry-title").string
    heading = unicode(heading)
    #print unicode(heading)

    #content = soup.find(attrs={'class': 'post-boilerplate boilerplate-before'})
    #print content

    p_array = soup.findAll("p")
    for p in p_array:
        content=content + ''.join(p.get_text(' ', strip=True))

    #print content

    date = soup.find(attrs={'class': 'the-time'})
    date = date.get_text(' ', strip=True)

    data = [heading,content,date]
    return data

def get_amount(data):
    amount=""
    token_list = data.split( );
    for token in token_list:
        if token.startswith('$'):
            amount=token
    return amount

def get_sector(content):
    sector=""
    
    flag=0
    for key in sectorDictionary.keys():
        for s in sectorDictionary[key]:
            if content.lower().find(s.lower())>=0:
                #print content.lower().find(s.lower())
                sector=key
                flag=1
                return sector  
    
    if flag==0:
        #print "Not found"
        return "other"

def create_json(sector,amount,date):
    jsonList.append({"sector":sector,"amount":amount,"date":date})

def main():
    data = get_content("http://venturebeat.com/2015/05/13/mediabong-no-not-that-kind-inhales-5m-for-u-s-expansion/")
    amount = get_amount(data[0])
    
    sector=get_sector(data[1])
    
    date = data[2]

    create_json(sector,amount,date)
    #-jsonList.append({"sector":"aasdf","amount":"328947","date":"4378 may 2015"})
    print jsonList
    
    #print sectorDictionary.keys()
    
    
    
main()    
input()
