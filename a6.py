import urllib.request as u
import xml.etree.ElementTree as ET

print("Part1")
root=ET.parse(source="cd_catalog.xml")

cds=root.findall("CD")
cost_total=0
total=0


for cd in cds:
    title=cd.find("TITLE")
    artist=cd.find("ARTIST")
    country=cd.find("COUNTRY")
    price=cd.find("PRICE")
    year=cd.find("YEAR")
    

    cost= float(price.text)
    cost_total+=cost
    
    average= cost_total/len(list(cds))

    if year.text=="1987":
        total+=1
        

    if country.text=="USA":
        artists= artist.text
        print("American Artists: ", artists)

print ("Amount of cds released in 1987:" , total, )
print("Total Cost: ", cost_total)
print("Average Cost: ", average)    
print("Number of CDS: ", len(list(cds)), "\n\n")


print("Part2")
root=ET.parse(source="books.xml")

books=root.findall("book")
total_cost=0


for book in books:
    cost=book.find("price")
    genre= book.find("genre")
    title=book.find("title")
    author=book.find("author")
    price= float(cost.text)

    

    attributes=list(book.items())

    for i in range(len(attributes)):        
        ids= attributes[i][1]
        if ids=="bk103":
            print("Book with id bk103:\n\tTitle:",title.text, "\n\tAuthor:", author.text, "\n\tPrice:", cost.text)

    if genre.text=="Computer":
     
        total_cost+=price


    if price > 10:
        print(title.text)
print("Total Cost: ", total_cost, "\n\n")


print("Part3")
conn = u.urlopen("http://rss.nytimes.com/services/xml/rss/nyt/World.xml")
lines=conn.read()
root=ET.XML(lines)

stories=root.findall("channel/item")


for story in stories:
    title=story.find("title")
    creator=story.find("{http://purl.org/dc/elements/1.1/}creator")
    country= story.find("category")
    attributes=list(country.items())
    
    
    image= story.find("{http://search.yahoo.com/mrss/}content")
    
    
    if image !=None:
        picture1= image.attrib
        picture= (picture1["url"])
        
    else:
        picture="No image"
    
    for i in range(len(attributes)):
        
        place= attributes[i][1]
        if place=="http://www.nytimes.com/namespaces/keywords/nyt_geo":
            country=country.text           
        else:
            country="No Country Information"

       

    #print(country,":", title.text, "(",creator.text,")\n", picture)
    #print("----------------------")
        
    
    
