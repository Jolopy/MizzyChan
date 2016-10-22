def indexPolitics():
    inf=open("PoliticsLinks.txt", 'r')
    outf=open("PoliticsLinksFinal.txt", 'w')
    
    for line in inf:
        line=inf.readline()
        if line.startswith("http://www.nytimes.com/2016/"):
            outf.write(line)
        if line.startswith("/2016/09") or line.startswith("/politics/2016/09") or line.startswith("/video/politics/2016/09"):
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
        if line.startswith("http://time.com/451"):
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
        if line.startswith("/2016/09"):
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
    
indexPolitics()
indexBusiness()