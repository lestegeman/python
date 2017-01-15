import urllib.request as u
import xml.etree.ElementTree as ET

conn=u.urlopen("https://itunes.apple.com/us/rss/topsongs/limit=10/xml")
lines=conn.read()
root=ET.XML(lines)

songs= root.findall("{http://www.w3.org/2005/Atom}entry")

for song in songs:
    title=song.find("{http://www.w3.org/2005/Atom}title")
    artist=song.find("{http://itunes.apple.com/rss}artist")
    album= song.find("{http://itunes.apple.com/rss}collection/{http://itunes.apple.com/rss}name")
    image= song.findall("{http://itunes.apple.com/rss}image")
    image=image[2].text
    
    link=song.findall("{http://www.w3.org/2005/Atom}link")
    link_att= link[1].attrib
    link2= link_att["href"]
    

    more_info= song.find("{http://www.w3.org/2005/Atom}link")
    more_info2=more_info.attrib
    more_info2=more_info2["href"]
    
