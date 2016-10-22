import requests
from bs4 import BeautifulSoup

def getPolitics():
    nytimesURL="http://www.nytimes.com/pages/politics"
    cnnURL="http://www.cnn.com/specials/politics/national-politics"
    foxnewsURL="http://www.foxnews.com/politics"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/Politics/Election"
    reutersnewsURL="http://www.reuters.com/politics"
    bbcnewsURL="http://www.bbc.com/news/election/us2016"
    #yahoonewsURL="https://www.yahoo.com/news/politics"
    nbcnewsURL="http://www.nbcnews.com/politics/2016-election"
    usatodaynewsURL="http://www.usatoday.com/section/global/elections-2016/"
    huffingtonpostnewsURL="http://www.huffingtonpost.com/section/politics"
    timenewsURL="http://www.time.com/politics"
    washingtonpostnewsURL="http://www.washingtonpost.com/politics/"
    guardiannewsURL="https://www.theguardian.com/us-news/us-elections-2016"
    #wsjnewsURL="http://www.wsj.com/news/politics"
    #latimesnewsURL="http://www.latimes.com/politics"
    nydailynewsURL="http://www.nydailynews.com/news/politics"
    #chicagotribunenewsURL="http://www.chicagotribune.com/news/nationworld/politics/"
   
    r_nytimes=requests.get(nytimesURL)
    r_CNN=requests.get(cnnURL)
    r_foxnews=requests.get(foxnewsURL)
    #r_cbsnews=requests.get(cbsnewsURL)
    r_abcnews=requests.get(abcnewsURL)
    r_reutersnews=requests.get(reutersnewsURL)
    r_bbcnews=requests.get(bbcnewsURL)
    #r_yahoonews=requests.get(yahoonewsURL)
    r_nbcnews=requests.get(nbcnewsURL)
    r_usatodaynews=requests.get(usatodaynewsURL)
    r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    r_washingtonpostnews=requests.get(washingtonpostnewsURL)
    r_guardiannews=requests.get(guardiannewsURL)
    #r_wsjnews=requests.get(wsjnewsURL)
    #r_latimesnews=requests.get(latimesnewsURL)
    r_nydailynews=requests.get(nydailynewsURL)
    #r_chicagotribunenews=requests.get(chicagotribunenewsURL)
    
    nytimesSoup=BeautifulSoup(r_nytimes.content, "lxml")
    cnnSoup=BeautifulSoup(r_CNN.content, "lxml")
    foxnewsSoup=BeautifulSoup(r_foxnews.content, "lxml")
    #cbsnewsSoup=BeautifulSoup(r_cbsnews.content, "lxml")
    abcnewsSoup=BeautifulSoup(r_abcnews.content, "lxml")
    reutersnewsSoup=BeautifulSoup(r_reutersnews.content, "lxml")
    bbcnewsSoup=BeautifulSoup(r_bbcnews.content, "lxml")
    #yahoonewsSoup=BeautifulSoup(r_yahoonews.content, "lxml")
    nbcnewsSoup=BeautifulSoup(r_nbcnews.content, "lxml")
    usatodaynewsSoup=BeautifulSoup(r_usatodaynews.content, "lxml")
    huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
    guardiannewsSoup=BeautifulSoup(r_guardiannews.content, "lxml")
    #wsjnewsSoup=BeautifulSoup(r_wsjnews.content, "lxml")
    #latimesnewsSoup=BeautifulSoup(r_latimesnews.content, "lxml")
    nydailynewsSoup=BeautifulSoup(r_nydailynews.content, "lxml")
    #chicagotribunenewsSoup=BeautifulSoup(r_chicagotribunenews.content, "lxml")
    
    nytimesLinks=nytimesSoup.find_all("a")
    cnnLinks=cnnSoup.find_all("a")
    foxnewsLinks=foxnewsSoup.find_all("a")
    #cbsnewsLinks=cbsnewsSoup.find_all("a")
    abcnewsLinks=abcnewsSoup.find_all("a")
    reutersnewsLinks=reutersnewsSoup.find_all("a")
    bbcnewsLinks=bbcnewsSoup.find_all("a")
    #yahoonewsLinks=yahoonewsSoup.find_all("a")
    nbcnewsLinks=nbcnewsSoup.find_all("a")
    usatodaynewsLinks=usatodaynewsSoup.find_all("a")
    huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,nbcnewsLinks,usatodaynewsLinks,huffingtonpostnewsLinks,timenewsLinks,
            washingtonpostnewsLinks,guardiannewsLinks,nydailynewsLinks]

    politicsLinks=[]
    pointer=0
    
    listLength=len(linkList)
    outf=open("PoliticsLinks.txt",'w')
    
    for i in range(listLength):
        for link in linkList[pointer]:
            if link.get("href") is None:
                continue
            else:
                politicsLinks.append(link.get("href"))
           
        pointer+=1

    for url in list(set(politicsLinks)):
        outf.write(url)
        outf.write('\n')
   
    outf.close()
    
def getBusiness():
    nytimesURL="http://www.nytimes.com/pages/business"
    cnnURL="http://www.money.cnn.com"
    foxnewsURL="http://www.foxbusiness.com"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/Business"
    reutersnewsURL="http://www.reuters.com/finance"
    bbcnewsURL="http://www.bbc.com/news/business"
    #yahoonewsURL="https://www.yahoo.com/news/politics"
    nbcnewsURL="http://www.nbcnews.com/business"
    usatodaynewsURL="http://www.usatoday.com/money/"
    huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
    timenewsURL="http://www.time.com/business"
    washingtonpostnewsURL="https://www.washingtonpost.com/business/"
    guardiannewsURL="https://www.theguardian.com/us/business"
    #wsjnewsURL="http://www.wsj.com/news/business"
    #latimesnewsURL="http://www.latimes.com/politics"
    #nydailynewsURL="http://www.nydailynews.com/news/politics"
    #chicagotribunenewsURL="http://www.chicagotribune.com/business"
   
    r_nytimes=requests.get(nytimesURL)
    r_CNN=requests.get(cnnURL)
    r_foxnews=requests.get(foxnewsURL)
    #r_cbsnews=requests.get(cbsnewsURL)
    r_abcnews=requests.get(abcnewsURL)
    r_reutersnews=requests.get(reutersnewsURL)
    r_bbcnews=requests.get(bbcnewsURL)
    #r_yahoonews=requests.get(yahoonewsURL)
    r_nbcnews=requests.get(nbcnewsURL)
    r_usatodaynews=requests.get(usatodaynewsURL)
    r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    r_washingtonpostnews=requests.get(washingtonpostnewsURL)
    r_guardiannews=requests.get(guardiannewsURL)
    #r_wsjnews=requests.get(wsjnewsURL)
    #r_latimesnews=requests.get(latimesnewsURL)
    #r_nydailynews=requests.get(nydailynewsURL)
    #r_chicagotribunenews=requests.get(chicagotribunenewsURL)
    
    nytimesSoup=BeautifulSoup(r_nytimes.content, "lxml")
    cnnSoup=BeautifulSoup(r_CNN.content, "lxml")
    foxnewsSoup=BeautifulSoup(r_foxnews.content, "lxml")
    #cbsnewsSoup=BeautifulSoup(r_cbsnews.content, "lxml")
    abcnewsSoup=BeautifulSoup(r_abcnews.content, "lxml")
    reutersnewsSoup=BeautifulSoup(r_reutersnews.content, "lxml")
    bbcnewsSoup=BeautifulSoup(r_bbcnews.content, "lxml")
    #yahoonewsSoup=BeautifulSoup(r_yahoonews.content, "lxml")
    nbcnewsSoup=BeautifulSoup(r_nbcnews.content, "lxml")
    usatodaynewsSoup=BeautifulSoup(r_usatodaynews.content, "lxml")
    huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
    guardiannewsSoup=BeautifulSoup(r_guardiannews.content, "lxml")
    #wsjnewsSoup=BeautifulSoup(r_wsjnews.content, "lxml")
    #latimesnewsSoup=BeautifulSoup(r_latimesnews.content, "lxml")
    #nydailynewsSoup=BeautifulSoup(r_nydailynews.content, "lxml")
    #chicagotribunenewsSoup=BeautifulSoup(r_chicagotribunenews.content, "lxml")
    
    nytimesLinks=nytimesSoup.find_all("a")
    cnnLinks=cnnSoup.find_all("a")
    foxnewsLinks=foxnewsSoup.find_all("a")
    #cbsnewsLinks=cbsnewsSoup.find_all("a")
    abcnewsLinks=abcnewsSoup.find_all("a")
    reutersnewsLinks=reutersnewsSoup.find_all("a")
    bbcnewsLinks=bbcnewsSoup.find_all("a")
    #yahoonewsLinks=yahoonewsSoup.find_all("a")
    nbcnewsLinks=nbcnewsSoup.find_all("a")
    usatodaynewsLinks=usatodaynewsSoup.find_all("a")
    huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,nbcnewsLinks,usatodaynewsLinks,huffingtonpostnewsLinks,timenewsLinks,
            washingtonpostnewsLinks,guardiannewsLinks]

    businessLinks=[]
    pointer=0
    
    listLength=len(linkList)
    outf=open("BusinessLinks.txt",'w')
    
    for i in range(listLength):
        for link in linkList[pointer]:
            if link.get("href") is None:
                continue
            else:
                businessLinks.append(link.get("href"))
           
        pointer+=1

    for url in list(set(businessLinks)):
        outf.write(url)
        outf.write('\n')
   
    outf.close()

getPolitics()
getBusiness()



   

    




