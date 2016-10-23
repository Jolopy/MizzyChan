import requests
from bs4 import BeautifulSoup

def getMemes():
    memep1URL="http://www.quickmeme.com/page/1/"
    memep2URL="http://www.quickmeme.com/page/2/"
    memep3URL="http://www.quickmeme.com/page/3/"
    memep4URL="http://www.quickmeme.com/page/4/"
    memep5URL="http://www.quickmeme.com/page/5/"
    memep6URL="http://www.quickmeme.com/page/6/"
    memep7URL="http://www.quickmeme.com/page/7/"
    memep8URL="http://www.quickmeme.com/page/8/"
    memep9URL="http://www.quickmeme.com/page/9/"
    memep10URL="http://www.quickmeme.com/page/10/"
    
    r_memep1=requests.get(memep1URL)
    r_memep2=requests.get(memep2URL)
    r_memep3=requests.get(memep3URL)
    r_memep4=requests.get(memep4URL)
    r_memep5=requests.get(memep5URL)
    r_memep6=requests.get(memep6URL)
    r_memep7=requests.get(memep7URL)
    r_memep8=requests.get(memep8URL)
    r_memep9=requests.get(memep9URL)
    r_memep10=requests.get(memep10URL)
    
    memep1Soup=BeautifulSoup(r_memep1.content, "lxml")
    memep2Soup=BeautifulSoup(r_memep2.content, "lxml")
    memep3Soup=BeautifulSoup(r_memep3.content, "lxml")
    memep4Soup=BeautifulSoup(r_memep4.content, "lxml")
    memep5Soup=BeautifulSoup(r_memep5.content, "lxml")
    memep6Soup=BeautifulSoup(r_memep6.content, "lxml")
    memep7Soup=BeautifulSoup(r_memep7.content, "lxml")
    memep8Soup=BeautifulSoup(r_memep8.content, "lxml")
    memep9Soup=BeautifulSoup(r_memep9.content, "lxml")
    memep10Soup=BeautifulSoup(r_memep10.content, "lxml")
    
    memep1Links=memep1Soup.find_all("a")
    memep2Links=memep2Soup.find_all("a")
    memep3Links=memep3Soup.find_all("a")
    memep4Links=memep4Soup.find_all("a")
    memep5Links=memep5Soup.find_all("a")
    memep6Links=memep6Soup.find_all("a")
    memep7Links=memep7Soup.find_all("a")
    memep8Links=memep8Soup.find_all("a")
    memep9Links=memep9Soup.find_all("a")
    memep10Links=memep10Soup.find_all("a")
    
    linkList=[memep1Links,memep2Links,memep3Links,memep4Links,memep5Links,memep6Links,memep7Links,
              memep8Links,memep9Links,memep10Links]
    
    memeLinks=[]
    
    pointer=0
    
    listLength=len(linkList)
    outf=open("MemeLinks.txt",'w')
    
    for i in range(listLength):
        for link in linkList[pointer]:
            if link.get("href") is None:
                continue
            else:
                memeLinks.append(link.get("href"))
           
        pointer+=1

    for url in list(set(memeLinks)):
        outf.write(url)
        outf.write('\n')
   
    outf.close()
    

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
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/politics"
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
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
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
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
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
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,nbcnewsLinks,usatodaynewsLinks,timenewsLinks,
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
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
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
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
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
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
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
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,nbcnewsLinks,usatodaynewsLinks,timenewsLinks,
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

def getGaming():
    
    n4gnewsURL="http://n4g.com/?tab=trending"
    cnetnewsURL="https://www.cnet.com/games/"
    engadgetnewsURL="https://www.engadget.com/gaming/"
    techradarnewsURL="http://www.techradar.com/news/gaming"
    digitalspynewsURL="http://www.digitalspy.com/gaming/"
    thevergenewsURL="http://www.theverge.com/games"
    polygonnewsURL="https://www.polygon.com/news"
    
    r_n4gnews=requests.get(n4gnewsURL)
    r_cnetnews=requests.get(cnetnewsURL)
    r_engadgetnews=requests.get(engadgetnewsURL)
    r_techradernews=requests.get(techradarnewsURL)
    r_digitalspynews=requests.get(digitalspynewsURL)
    r_thevergenews=requests.get(thevergenewsURL)
    r_polygonnews=requests.get(polygonnewsURL)
    
    n4gnewsSoup=BeautifulSoup(r_n4gnews.content, "lxml")
    cnetnewsSoup=BeautifulSoup(r_cnetnews.content, "lxml")
    engadgetnewsSoup=BeautifulSoup(r_engadgetnews.content, "lxml")
    techradarnewsSoup=BeautifulSoup(r_techradernews.content, "lxml")
    digitalspynewsSoup=BeautifulSoup(r_digitalspynews.content, "lxml")
    thevergenewsSoup=BeautifulSoup(r_thevergenews.content, "lxml")
    polygonnewsSoup=BeautifulSoup(r_polygonnews.content, "lxml")
    
    n4gnewsLinks=n4gnewsSoup.find_all("a")
    cnetnewsLinks=cnetnewsSoup.find_all("a")
    engadgetnewsLinks=engadgetnewsSoup.find_all("a")
    techradarnewsLinks=techradarnewsSoup.find_all("a")
    digitalspynewsLinks=techradarnewsSoup.find_all("a")
    thevergenewsLinks=thevergenewsSoup.find_all("a")
    polygonnewsLinks=polygonnewsSoup.find_all("a")
    
    linkList=[n4gnewsLinks,cnetnewsLinks,engadgetnewsLinks,techradarnewsLinks,digitalspynewsLinks,
              thevergenewsLinks,polygonnewsLinks]
    
    gamingLinks=[]
    pointer=0
    
    listLength=len(linkList)
    outf=open("GamingLinks.txt",'w')
    
    for i in range(listLength):
        for link in linkList[pointer]:
            if link.get("href") is None:
                continue
            else:
                gamingLinks.append(link.get("href"))
           
        pointer+=1

    for url in list(set(gamingLinks)):
        outf.write(url)
        outf.write('\n')
   
    outf.close()
    
def getWorldNews():
    
    nytimesURL="http://www.nytimes.com/pages/world"
    cnnURL="http://www.cnn.com/world"
    foxnewsURL="http://www.foxnews.com/world"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/International"
    reutersnewsURL="http://www.reuters.com/news/world"
    bbcnewsURL="http://www.bbc.com/news/world"
    #yahoonewsURL="https://www.yahoo.com/news/politics"
    nbcnewsURL="http://www.nbcnews.com/news/world"
    usatodaynewsURL="http://www.usatoday.com/news/world"
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
    timenewsURL="http://www.time.com/world"
    #washingtonpostnewsURL="https://www.washingtonpost.com/world/"
    guardiannewsURL="https://www.theguardian.com/world"
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
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    #r_washingtonpostnews=requests.get(washingtonpostnewsURL)
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
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    #washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
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
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    #washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,nbcnewsLinks,usatodaynewsLinks,timenewsLinks,guardiannewsLinks]

    businessLinks=[]
    pointer=0
    
    listLength=len(linkList)
    outf=open("WorldNewsLinks.txt",'w')
    
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
    
    
def getUSNews():
    
    nytimesURL="http://www.nytimes.com/section/us"
    cnnURL="http://www.cnn.com/us"
    foxnewsURL="http://www.foxnews.com/us"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/US"
    reutersnewsURL="http://www.reuters.com/news/us"
    bbcnewsURL="http://www.bbc.com/news/world/us_and_canada"
    #yahoonewsURL="https://www.yahoo.com/news/politics"
    nbcnewsURL="http://www.nbcnews.com/news/us-news"
    usatodaynewsURL="http://www.usatoday.com/news/nation"
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
    timenewsURL="http://www.time.com/us"
    #washingtonpostnewsURL="https://www.washingtonpost.com/world/"
    guardiannewsURL="https://www.theguardian.com/us"
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
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    #r_washingtonpostnews=requests.get(washingtonpostnewsURL)
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
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    #washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
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
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    #washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,nbcnewsLinks,usatodaynewsLinks,timenewsLinks,guardiannewsLinks]

    businessLinks=[]
    pointer=0
    
    listLength=len(linkList)
    outf=open("USNewsLinks.txt",'w')
    
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

def getEntertainment():
    
    nytimesURL="http://www.nytimes.com/section/arts"
    cnnURL="http://www.cnn.com/entertainment"
    foxnewsURL="http://www.foxnews.com/entertainment"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/Entertainment"
    reutersnewsURL="http://www.reuters.com/news/entertainment"
    bbcnewsURL="http://www.bbc.com/news/entertainment_and_arts"
    #yahoonewsURL="https://www.yahoo.com/news/politics"
    #nbcnewsURL="http://www.nbcnews.com/pop-culture"
    usatodaynewsURL="http://www.usatoday.com/life"
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
    timenewsURL="http://www.time.com/entertainment"
    #washingtonpostnewsURL="https://www.washingtonpost.com/world/"
    guardiannewsURL="https://www.theguardian.com/us/culture"
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
    #r_nbcnews=requests.get(nbcnewsURL)
    r_usatodaynews=requests.get(usatodaynewsURL)
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    #r_washingtonpostnews=requests.get(washingtonpostnewsURL)
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
    #nbcnewsSoup=BeautifulSoup(r_nbcnews.content, "lxml")
    usatodaynewsSoup=BeautifulSoup(r_usatodaynews.content, "lxml")
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    #washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
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
    #nbcnewsLinks=nbcnewsSoup.find_all("a")
    usatodaynewsLinks=usatodaynewsSoup.find_all("a")
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    #washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,usatodaynewsLinks,timenewsLinks,guardiannewsLinks]

    businessLinks=[]
    pointer=0
    
    listLength=len(linkList)
    outf=open("EntertainmentLinks.txt",'w')
    
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
    
def getSports():
    
    nytimesURL="http://www.nytimes.com/section/sports"
    cnnURL="http://www.bleacherrepot.com"
    #foxnewsURL="http://www.foxnews.com/entertainment"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/Sports"
    reutersnewsURL="http://www.reuters.com/news/sports"
    #bbcnewsURL="http://www.bbc.com/sport"
    yahoonewsURL="https://www.yahoo.com/news/politics"
    nbcnewsURL="http://www.nbcsports.com/"
    usatodaynewsURL="http://www.usatoday.com/sports"
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
    timenewsURL="http://www.time.com/sports"
    #washingtonpostnewsURL="https://www.washingtonpost.com/world/"
    guardiannewsURL="https://www.theguardian.com/us/sport"
    #wsjnewsURL="http://www.wsj.com/news/business"
    #latimesnewsURL="http://www.latimes.com/politics"
    #nydailynewsURL="http://www.nydailynews.com/news/politics"
    #chicagotribunenewsURL="http://www.chicagotribune.com/business"
   
    r_nytimes=requests.get(nytimesURL)
    r_CNN=requests.get(cnnURL)
    #r_foxnews=requests.get(foxnewsURL)
    #r_cbsnews=requests.get(cbsnewsURL)
    r_abcnews=requests.get(abcnewsURL)
    r_reutersnews=requests.get(reutersnewsURL)
    #r_bbcnews=requests.get(bbcnewsURL)
    #r_yahoonews=requests.get(yahoonewsURL)
    r_nbcnews=requests.get(nbcnewsURL)
    r_usatodaynews=requests.get(usatodaynewsURL)
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    #r_washingtonpostnews=requests.get(washingtonpostnewsURL)
    r_guardiannews=requests.get(guardiannewsURL)
    #r_wsjnews=requests.get(wsjnewsURL)
    #r_latimesnews=requests.get(latimesnewsURL)
    #r_nydailynews=requests.get(nydailynewsURL)
    #r_chicagotribunenews=requests.get(chicagotribunenewsURL)
    
    nytimesSoup=BeautifulSoup(r_nytimes.content, "lxml")
    cnnSoup=BeautifulSoup(r_CNN.content, "lxml")
    #foxnewsSoup=BeautifulSoup(r_foxnews.content, "lxml")
    #cbsnewsSoup=BeautifulSoup(r_cbsnews.content, "lxml")
    abcnewsSoup=BeautifulSoup(r_abcnews.content, "lxml")
    reutersnewsSoup=BeautifulSoup(r_reutersnews.content, "lxml")
    #bbcnewsSoup=BeautifulSoup(r_bbcnews.content, "lxml")
    #yahoonewsSoup=BeautifulSoup(r_yahoonews.content, "lxml")
    nbcnewsSoup=BeautifulSoup(r_nbcnews.content, "lxml")
    usatodaynewsSoup=BeautifulSoup(r_usatodaynews.content, "lxml")
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    #washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
    guardiannewsSoup=BeautifulSoup(r_guardiannews.content, "lxml")
    #wsjnewsSoup=BeautifulSoup(r_wsjnews.content, "lxml")
    #latimesnewsSoup=BeautifulSoup(r_latimesnews.content, "lxml")
    #nydailynewsSoup=BeautifulSoup(r_nydailynews.content, "lxml")
    #chicagotribunenewsSoup=BeautifulSoup(r_chicagotribunenews.content, "lxml")
    
    nytimesLinks=nytimesSoup.find_all("a")
    cnnLinks=cnnSoup.find_all("a")
    #foxnewsLinks=foxnewsSoup.find_all("a")
    #cbsnewsLinks=cbsnewsSoup.find_all("a")
    abcnewsLinks=abcnewsSoup.find_all("a")
    reutersnewsLinks=reutersnewsSoup.find_all("a")
    #bbcnewsLinks=bbcnewsSoup.find_all("a")
    #yahoonewsLinks=yahoonewsSoup.find_all("a")
    nbcnewsLinks=nbcnewsSoup.find_all("a")
    usatodaynewsLinks=usatodaynewsSoup.find_all("a")
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    #washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,abcnewsLinks,reutersnewsLinks,
            nbcnewsLinks,usatodaynewsLinks,timenewsLinks,guardiannewsLinks]

    businessLinks=[]
    pointer=0
    
    listLength=len(linkList)
    outf=open("SportsLinks.txt",'w')
    
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
    
def getTech():
    
    nytimesURL="http://www.nytimes.com/pages/technology"
    cnnURL="http://www.money.cnn.com/technology"
    foxnewsURL="http://www.foxnews.com/tech"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/Technology"
    reutersnewsURL="http://www.reuters.com/news/technology"
    bbcnewsURL="http://www.bbc.com/news/technology"
    #yahoonewsURL="https://www.yahoo.com/news/politics"
    #nbcnewsURL="http://www.nbcnews.com/tech"
    usatodaynewsURL="http://www.usatoday.com/tech"
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
    timenewsURL="http://www.time.com/tech"
    #washingtonpostnewsURL="https://www.washingtonpost.com/world/"
    guardiannewsURL="https://www.theguardian.com/us/technology"
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
    #r_nbcnews=requests.get(nbcnewsURL)
    r_usatodaynews=requests.get(usatodaynewsURL)
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    #r_washingtonpostnews=requests.get(washingtonpostnewsURL)
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
    #nbcnewsSoup=BeautifulSoup(r_nbcnews.content, "lxml")
    usatodaynewsSoup=BeautifulSoup(r_usatodaynews.content, "lxml")
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    #washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
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
    #nbcnewsLinks=nbcnewsSoup.find_all("a")
    usatodaynewsLinks=usatodaynewsSoup.find_all("a")
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    #washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,usatodaynewsLinks,timenewsLinks,guardiannewsLinks]

    businessLinks=[]
    pointer=0
    
    listLength=len(linkList)
    outf=open("TechLinks.txt",'w')
    
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
getMemes()
getGaming()
getWorldNews()
getUSNews()
getEntertainment()
getSports()
getTech()

def indexMemes():
    inf=open("MemeLinks.txt", 'r')
    outf=open("MemeLinksFinal.txt", 'w')
    
    for line in inf:
        if line.startswith("/p/"):
            outf.write("http://www.quickmeme.com")
            outf.write(line)
    inf.close()
    outf.close()
    
def indexPolitics():
    inf=open("PoliticsLinks.txt", 'r')
    outf=open("PoliticsLinksFinal.txt", 'w')
    
    for line in inf:
        line=inf.readline()
        if line.startswith("http://www.nytimes.com/2016/"):
            outf.write(line)
        if line.startswith("/2016/10/") or line.startswith("/politics/2016/09") or line.startswith("/video/politics/2016/09"):
            outf.write("http://www.cnn.com")
            outf.write(line)
        if line.startswith("http://www.foxnews.com/politics/2016/09/"):
            outf.write(line)
        if line.startswith("http://abcnews.go.com/Politics/"):
            outf.write(line)
        if line.startswith("/article/us-usa-election"):
            outf.write("http://www.reuters.com")
            outf.write(line)
        if line.startswith("/news/election-us-2016"):
            outf.write("http://www.bbc.com")
            outf.write(line)
        if line.startswith("/politics/2016-election/") and "primaries" not in line:
            outf.write("http://nbcnews.com")
            outf.write(line)
        if line.startswith("/story/news/politics/"):
            outf.write("http://www.usatoday.com")
            outf.write(line)
        if line.startswith("http://www.huffingtonpost.com/entry/"):
            outf.write(line)
        if line.startswith("http://time.com/453") or line.startswith("http://time.com/454"):
            #the 451 will change based on time
            outf.write(line)
        if line.startswith("https://www.washingtonpost.com/news/post-politics/wp/2016/") or line.startswith("https://www.washingtonpost.com/news/the-fix/wp/2016/"):
            outf.write(line)
        if line.startswith("https://www.theguardian.com/us-news/2016/" or "https://www.theguardian.com/us-news/video/2016"):
            outf.write(line)
        
        if line.startswith("http://www.nydailynews.com/news/politics"):
            outf.write(line)
       
        
    inf.close()
    outf.close()


def indexBusiness():
    inf=open("BusinessLinks.txt", 'r')
    outf=open("BusinessLinksFinal.txt", 'w')
    
    for line in inf:
        line=inf.readline()
        if line.startswith("http://www.nytimes.com/2016/"):
            outf.write(line)
        if line.startswith("/2016/10/"):
            outf.write("http://www.money.cnn.com")
            outf.write(line)
        if line.startswith("/markets/2016") or line.startswith("/politics/2016") or line.startswith("/features/2016") or            line.startswith("/investing/2016"):
            outf.write("http://www.foxbusiness.com")
            outf.write(line)
        if line.startswith("http://abcnews.go.com/Business/"):
            outf.write(line)
        if line.startswith("/Business/"):
            outf.write("http://www.abcnews.go.com")
            outf.write(line)
        if line.startswith("/article/") or line.startswith("/video/2016"):
            outf.write("http://www.reuters.com")
            outf.write(line)
        if line.startswith("/news/business-1") or line.startswith("/news/business-2") or line.startswith("/news/business-3"):
            outf.write("http://www.bbc.com")
            outf.write(line)
        if line.startswith("/business/consumer/") or line.startswith("/business/personal-finance/") or line.startswith("/business/economy/") or line.startswith("/business/markets/"):
            outf.write("http://nbcnews.com")
            outf.write(line)
        if line.startswith("/story/money/"):
            outf.write("http://www.usatoday.com/money")
            outf.write(line)
        if line.startswith("http://www.huffingtonpost.com/entry/"):
            outf.write(line)
        if line.startswith("http://time.com/451"):
            #the 451 will change based on time
            outf.write(line)
        if line.startswith("https://www.washingtonpost.com/news/business/economy/") or line.startswith("https://www.washingtonpost.com/news/on-small-business/wp/2016/") or line.startswith("https://www.washingtonpost.com/news/wonk/wp/2016/") or line.startswith("https://www.washingtonpost.com/news/on-leadership/wp/2016/") or line.startswith("https://www.washingtonpost.com/news/get-there/wp/2016/") or line.startswith("https://www.washingtonpost.com/news/the-swtich/wp/2016/") or line.startswith("https://www.washingtonpost.com/news/capital-business/wp/2016/"):
            outf.write(line)
        if line.startswith("https://www.theguardian.com/business/2016/") or line.startswith("https://www.theguardian.com/us-news/2016/") or line.startswith("https://www.theguardian.com/technology/2016/") or line.startswith("https://www.theguardian.com/environment/2016/") or line.startswith("https://www.theguardian.com/world/2016/") or line.startswith("https://www.theguardian.com/sustainable-business/2016/"):
            outf.write(line)
        
        
        
    inf.close()
    outf.close()

def indexGaming():
    
    inf=open("GamingLinks.txt", 'r')
    outf=open("GamingLinksFinal.txt", 'w')
    
    for line in inf:
        if line.startswith("/news/1"):
            outf.write("http://n4g.com")
            outf.write(line)
        if line.startswith("https://www.cnet.com/videos/") or line.startswith("http://www.cnet.com/news/"):
            outf.write(line)
        if line.startswith("/2016/"):
            outf.write("https://www.engadget.com")
            outf.write(line)
        if line.startswith("http://www.techradar.com/news/") or line.startswith("http://www.techradar.com/reviews/"):
            outf.write(line)
        if line.startswith("/gaming/news/"):
            outf.write("http://www.digitalspy.com")
            outf.write(line)
        if line.startswith("http://www.theverge.com/2016/"):
            outf.write(line)
        if line.startswith("https://www.polygon.com/2016/"):
            outf.write(line)
        
def indexWorldNews():
    
    inf=open("WorldNewsLinks.txt", 'r')
    outf=open("WorldNewsLinksFinal.txt", 'w')
    
    for line in inf:
        line=inf.readline()
        if line.startswith("http://www.nytimes.com/2016/"):
            outf.write(line)
        if line.startswith("/2016/10/"):
            outf.write("http://www.cnn.com")
            outf.write(line)
        if line.startswith("/world/2016/10/"):
            outf.write("http://www.foxnews.com")
            outf.write(line)
        if line.startswith("/International/wireStory"):
            outf.write("http://www.abcnews.go.com")
            outf.write(line)
        if line.startswith("/article/") or line.startswith("/video/2016/10/"):
            outf.write("http://www.reuters.com")
            outf.write(line)
        if line.startswith("/news/world-africa") or line.startswith("/news/world-europe") or line.startswith("/news/world-us"):
            outf.write("http://www.bbc.com")
            outf.write(line)
        if line.startswith("/news/world/"):
            outf.write("http://nbcnews.com")
            outf.write(line)
        if line.startswith("/story/news/world/2016/10/"):
            outf.write("http://www.usatoday.com")
            outf.write(line)
        if line.startswith("http://www.huffingtonpost.com/entry/"):
            outf.write(line)
        if line.startswith("http://time.com/454") or line.startswith("http://time.com/453"):
            #the 451 will change based on time
            outf.write(line)
        if line.startswith("https://www.theguardian.com/world/2016/oct/"):
            outf.write(line)
        
        
        
    inf.close()
    outf.close()

def indexUSNews():
    
    inf=open("USNewsLinks.txt", 'r')
    outf=open("USNewsLinksFinal.txt", 'w')
    
    for line in inf:
        line=inf.readline()
        if line.startswith("http://www.nytimes.com/2016/10/"):
            outf.write(line)
        if line.startswith("/2016/10/"):
            outf.write("http://www.cnn.com")
            outf.write(line)
        if line.startswith("/us/2016/10/"):
            outf.write("http://www.foxnews.com")
            outf.write(line)
        if line.startswith("/US/wireStory/"):
            outf.write("http://www.abcnews.go.com")
            outf.write(line)
        if line.startswith("/article/") or line.startswith("/video/2016/10/"):
            outf.write("http://www.reuters.com")
            outf.write(line)
        if line.startswith("/news/election-us") or line.startswith("/news/world-us"):
            outf.write("http://www.bbc.com")
            outf.write(line)
        if line.startswith("/news/us-news/"):
            outf.write("http://nbcnews.com")
            outf.write(line)
        if line.startswith("/story/news/nation-now/2016/10/"):
            outf.write("http://www.usatoday.com")
            outf.write(line)
        if line.startswith("http://www.huffingtonpost.com/entry/"):
            outf.write(line)
        if line.startswith("http://time.com/454") or line.startswith("http://time.com/453"):
            #the 451 will change based on time
            outf.write(line)
        if line.startswith("https://www.theguardian.com/us-news/2016/oct/"):
            outf.write(line)
        
        
        
    inf.close()
    outf.close()
    
def indexEntertainment():
    
    inf=open("EntertainmentLinks.txt", 'r')
    outf=open("EntertainmentLinksFinal.txt", 'w')
    
    for line in inf:
        line=inf.readline()
        if line.startswith("http://www.nytimes.com/2016/10/"):
            outf.write(line)
        if line.startswith("/2016/10/"):
            outf.write("http://www.cnn.com")
            outf.write(line)
        if line.startswith("/entertainment/2016/10/"):
            outf.write("http://www.foxnews.com")
            outf.write(line)
        if line.startswith("/Entertainment/"):
            outf.write("http://www.abcnews.go.com")
            outf.write(line)
        if line.startswith("/article/") or line.startswith("/video/2016/10/"):
            outf.write("http://www.reuters.com")
            outf.write(line)
        if line.startswith("/news/entertainment-arts"):
            outf.write("http://www.bbc.com")
            outf.write(line)
        if line.startswith("/pop-culture/"):
            outf.write("http://nbcnews.com")
            outf.write(line)
        if line.startswith("/story/life/2016/10/"):
            outf.write("http://www.usatoday.com")
            outf.write(line)
        if line.startswith("http://www.huffingtonpost.com/entry/"):
            outf.write(line)
        if line.startswith("http://time.com/454") or line.startswith("http://time.com/453"):
            #the 451 will change based on time
            outf.write(line)
        if line.startswith("https://www.theguardian.com/tv-and-radio/2016/oct/") or line.startswith("https://www.theguardian.com/music/2016/oct/") or line.startswith("https://www.theguardian.com/books/2016/oct/") or line.startswith("https://www.theguardian.com/culture/2016/oct/"):
            outf.write(line)

def indexSports():
    
    inf=open("SportsLinks.txt", 'r')
    outf=open("SportsLinksFinal.txt", 'w')
    
    for line in inf:
        line=inf.readline()
        if line.startswith("http://www.nytimes.com/2016/10/"):
            outf.write(line)
        if line.startswith("/articles/267"):
            outf.write("http://www.bleacherreport.com")
            outf.write(line)
        if line.startswith("/entertainment/2016/10/"):
            outf.write("http://www.foxnews.com")
            outf.write(line)
        if line.startswith("/Sports/wireStory/"):
            outf.write("http://www.abcnews.go.com")
            outf.write(line)
        if line.startswith("/article/"):
            outf.write("http://www.reuters.com")
            outf.write(line)
        if line.startswith("/news/entertainment-arts"):
            outf.write("http://www.bbc.com")
            outf.write(line)
        if line.startswith("http://nhl.nbcsports.com/2016/10/") or line.startswith("http://mlb.nbcsports.com/2016/10/") or line.startswith("http://nascar.nbcsports.com/2016/10/") or line.startswith("http://nhl.nbcsports.com/2016/10/") or line.startswith("http://soccer.nbcsports.com/2016/10/") or line.startswith("http://nba.nbcsports.com/2016/10/"):
            outf.write(line)
        if line.startswith("/story/sports/mlb/2016/10/") or line.startswith("/story/sports/ncaaf/2016/10/") or line.startswith("/story/sports/nfl/2016/10/") or line.startswith("/story/sports/nba/2016/10/") or line.startswith("/story/sports/nascar/2016/10/"):
            outf.write("http://www.usatoday.com/")
            outf.write(line)
        if line.startswith("http://www.huffingtonpost.com/entry/"):
            outf.write(line)
        if line.startswith("http://time.com/454") or line.startswith("http://time.com/453"):
            #the 451 will change based on time
            outf.write(line)
        if line.startswith("https://www.theguardian.com/sport/2016/oct/"):
            outf.write(line)
        
        
    inf.close()
    outf.close()

def indexTech():
    
    inf=open("TechLinks.txt", 'r')
    outf=open("TechLinksFinal.txt", 'w')
    
    for line in inf:
        line=inf.readline()
        if line.startswith("http://www.nytimes.com/2016/10/"):
            outf.write(line)
        if line.startswith("/2016/10/"):
            outf.write("http://www.money.cnn.com")
            outf.write(line)
        if line.startswith("http://www.foxnews.com/tech/2016/10/"):
            outf.write(line)
        if line.startswith("/Technology/wireStory/"):
            outf.write("http://www.abcnews.go.com")
            outf.write(line)
        if line.startswith("/article/") or line.startswith("/video/2016/10/"):
            outf.write("http://www.reuters.com")
            outf.write(line)
        if line.startswith("/news/technology-"):
            outf.write("http://www.bbc.com")
            outf.write(line)
        if line.startswith("http://nhl.nbcsports.com/2016/10/") or line.startswith("http://mlb.nbcsports.com/2016/10/") or line.startswith("http://nascar.nbcsports.com/2016/10/") or line.startswith("http://nhl.nbcsports.com/2016/10/") or line.startswith("http://soccer.nbcsports.com/2016/10/") or line.startswith("http://nba.nbcsports.com/2016/10/"):
            outf.write(line)
        if line.startswith("/story/tech/2016/10/") or line.startswith("/story/tech/news/2016/10/") :
            outf.write("http://www.usatoday.com/")
            outf.write(line)
        if line.startswith("http://www.huffingtonpost.com/entry/"):
            outf.write(line)
        if line.startswith("http://time.com/454") or line.startswith("http://time.com/453"):
            #the 451 will change based on time
            outf.write(line)
        if line.startswith("https://www.theguardian.com/technology/2016/oct/"):
            outf.write(line)
        
        
    inf.close()
    outf.close()
    
indexWorldNews()    
indexPolitics()
indexBusiness()
indexMemes()
indexGaming()
indexUSNews()
indexEntertainment()
indexSports()
indexTech()
    




