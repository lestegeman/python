import urllib.request as u
import os
import datetime

print("Part 1")
def getContent(url):
    name= os.path.basename(url)
    info= u.urlopen(url)
    content= info.readlines()

    file= open(name, "w")

    for i in range(len(content)):
        lines= content[i].decode("utf-8")
        file.write(lines)

    file.close()
    info.close()

getContent("http://www.cs.indiana.edu/~amutsudd/index.html")
getContent("http://www.york.ac.uk/teaching/cws/wws/webpage1.html")


print("Part 2")

def getStockData(company="GOOG"):

    baseurl= "http://quote.yahoo.com/d/quotes.csv?s=%s&f=sl1d1t1c1ohgvj1pp2owern&e=.csv"

    url= baseurl % company
    
    conn=u.urlopen(url)
    content=conn.readlines()
    content=content[0].decode("utf-8")
    lst=content.split(",")
    
    company1= lst[0]
    company1= company.strip('""')
    
    trade= lst[1]
    
    date=lst[2]
    date=date.strip('""')
    date= date.split("/")
    month= int(date[0])
    day= int(date[1])
    year= int(date[2])
    date2= datetime.date(year, month, day)
    date2= date2.strftime("%b %d, %Y")

    change=lst[4]
    
    
    print("The last trade for %s was %s and the change was %s on %s " %(company1, trade, change,date2))

getStockData()

def main():
    co=["PCLN", "AMZN", "MSFT", "EBAY", "NFLX"]


    for i in co:
        getStockData(company=i)

main()

print ("Part 3")

def earthquakeInfo(src, magnitude):
    if magnitude== "2.5" or magnitude =="5" or magnitude=="7":
        url="http://earthquake.usgs.gov/earthquakes/catalogs/eqs7day-M%s.txt"
        url= url %(magnitude)
        week=0
        today=0
        total=0
        name= os.path.basename(url)
        info= u.urlopen(url)
        content= info.readlines()
        content.pop(0)
        
        for i in range(len(content)):
            content[i]=content[i].decode("utf-8")
            quake= content[i].split(",")
            week+=1
            source= quake[0]
            if source== src:
                total+=1

            now= datetime.date.today()
            now2= now.strftime(" %B %d")
            now2= now2.replace("0", " ")
            
            date= quake[4]
            
            if now2==date:
                today+=1
    
        
        print ("Today's Date: %s \nMagnitude: %s\nTotal number of Earthquakes past 7 days: %s \nEarthquakes today: %s\nEarthquake at source %s: %s" %(now, magnitude, week, today, src, total)) 

    else:
        print("No such information exists. Enter magnitude of 2.5, 5, or 7")
    

earthquakeInfo("ak", "2.5")



