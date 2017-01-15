#!/l/python3/bin/python
import urllib.request as u
import xml.etree.ElementTree as ET
import cgi

#Gets user inputs from the forms on the HTML page
form=cgi.FieldStorage()
#gets the user input of the search_by form and allow them to search for songs, number, and country
search= form.getfirst("search_by", "Top Songs")
number=form.getfirst("number", "10")
country=form.getfirst("country","United States")

#determines what to search iTunes database for from what the user inputed they wanted
if search=="Top Songs":
    search_by="topsongs"
    phrase="Songs"
elif search=="Top Albums":
    search_by="topalbums"
    phrase="Albums"
elif search=="Top Music Videos":
    search_by="topmusicvideos"
    phrase="Music Videos"

#takes what the user inputs and searches iTunes for the abbreviations they use

if country=="United States":
    country2="us"
elif country=="Turkey":
    country2="tr"
elif country=="India":
    country2="in"
try:
    conn=u.urlopen("https://itunes.apple.com/%s/rss/%s/limit=%s/xml"%(country2,search_by,number))
    #gives an error if the input cannot be found

except:
    print("Content-type:text/html\n")
    print("Invalid Search")
    #if it can be found this reads the lines in entry

else:
    print("Content-type:text/html\n")
    lines=conn.read()
    root=ET.XML(lines)   

    songs= root.findall("{http://www.w3.org/2005/Atom}entry")

    #adds html to the page to make it look pretty
    header="""   
    <head>
    <style type="text/css">
    body{background-color:#D2FFF0;}  #makes background seafoam green
    h1{font-family:arial; font-size:40px;}   #changes headerfont to arial
    p{font-family:arial; font-size:20px;}    #changes all paragraphfont to arial
    </style>
    </head>
    <title>Top Songs</title>
    <body>
    <center>
    <h1> Top %s %s from %s </h1>
    <hr><hr>
    </center>"""%(number,phrase, country)
    print(header)
    #if the users wants to see 'top songs' this finds the information about it

    if search=="Top Songs":
        for song in songs:
            title=song.find("{http://www.w3.org/2005/Atom}title")   #finds the title text
            title=title.text
            artist=song.find("{http://itunes.apple.com/rss}artist")
            #finds the artist text
            artist=artist.text
            album= song.find("{http://itunes.apple.com/rss}collection/{http://itunes.apple.com/rss}na$
            #finds the album text
            album=album.text
            image= song.findall("{http://itunes.apple.com/rss}image")
            #finds the image
            image=image[2].text
            #there are several image sizes so this takes the third size of 170
            query= title + artist
            # concatentates title and artist so that the song can be searched in youtube
    
            picture="""<img src="%s" border=2>"""%(image)
            # makes image into html formatting
    
            link=song.findall("{http://www.w3.org/2005/Atom}link")
            link_att= link[1].attrib
            link2= link_att["href"]
            #finds link to audio of the song by searching attributes of that particular element
            
            more_info= song.find("{http://www.w3.org/2005/Atom}link")
            #adds a link to the iTunes page to get more info about the song
            more_info2=more_info.attrib
            more_info2=more_info2["href"]
            
            htmlstring="""
            <center>
            <p> %s
            </br> %s
            </br> %s
            </br> %s
            </br> <a href="%s">Listen</a> || <a href="%s"> More info</a>
            <form method=POST action="http://www.youtube.com/results?search_query=%s" target="_blank">
            </br> <input type=submit value="Youtube">
            </p>
            </center>
            <hr>
            </body>"""%(title, artist, album, picture,link2, more_info2,query)
            #prints the information it retrieved from each song
            print(htmlstring)
            
        #takes user input and finds the information about it
    elif search=="Top Albums":
        for song in songs:
            title=song.find("{http://www.w3.org/2005/Atom}title")   #finds the title of the album in $
            title=title.text
            artist=song.find("{http://itunes.apple.com/rss}artist")
            artist=artist.text
            
            image= song.findall("{http://itunes.apple.com/rss}image")
            #gets the image
            image=image[2].text                                                                      
            query= title + artist
            
            picture="""<img src="%s" border=2>"""%(image)
            #makes sure the image appears as an image
            
            more_info= song.find("{http://www.w3.org/2005/Atom}link")
            #adds a link to iTunes page for more info on album
            more_info2=more_info.attrib
            more_info2=more_info2["href"]

            htmlstring="""
            <center>
            <p> %s
            </br> %s
            </br> %s
            </br>  <a href="%s"> More info</a>
            <form method=POST action="http://www.youtube.com/results?search_query=%s" target="_blank">
            </br> <input type=submit value="Youtube">
            </p>
            </center>
            <hr>
            </body>"""%(title, artist, picture, more_info2, query)
            #prints the information about the albums
            print(htmlstring)
            
            #finds all information regarding what music videos the user wants to see
            
    elif search=="Top Music Videos":
        for song in songs:
            title=song.find("{http://www.w3.org/2005/Atom}title")
            #finds title of top music videos
            title=title.text
            artist=song.find("{http://itunes.apple.com/rss}artist")
            #finds artist of top music videos
            artist=artist.text
            image= song.findall("{http://itunes.apple.com/rss}image")
            #finds the image of the video album
            image=image[2].text
            query= title + artist
            
            picture="""<img src="%s" border=2>"""%(image)
            #makes sure the image appears
            
            link=song.findall("{http://www.w3.org/2005/Atom}link")
            link_att= link[1].attrib
            link2= link_att["href"]

            
            more_info= song.find("{http://www.w3.org/2005/Atom}link")
            #adds link to iTunes to get more info about album
            more_info2=more_info.attrib
            more_info2=more_info2["href"]
 
            htmlstring="""  
            <center>
            <p> %s
            </br> %s
            </br> %s
            </br> <a href="%s">Watch</a> || <a href="%s"> More info</a>
            <form method=POST action="http://www.youtube.com/results?search_query=%s" target="_blank">
            </br> <input type=submit value="Youtube">
            </p>
            </center>
            <hr>
            </body>"""%(title, artist, picture,link2, more_info2, query)
            #prints the information about the music videos
            print(htmlstring)
                                                      
            
            
