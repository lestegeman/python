#!/l/python3/bin/python
import cgi
import mysql.connector as m
con = m.connect(host="silo.soic.indiana.edu", port =3306, user="itunesdb", passwd="it+db=my+sql",
db="itunesdb")
#makes a connection to the database
cursor = con.cursor()

print("Content-type:text/html\n")

form= cgi.FieldStorage()
# collects information from the forms in the html page
search= form.getfirst("song","Rock")
#gets information from form called song, if no information is entered then Rock is the default
searchby="genre"
#variable to search by genre
searchby1="artist"
#variable to search by artist
searchby2="title"
#variable to search by title

filter= form.getfirst("options","genre")
#gets information from form called options, if no information is entered then genre is the default

#This portion takes the user input and searches the database for a match
if filter=="genre":
        query="SELECT * FROM songs WHERE " + searchby +  " LIKE '%" + search + "%' limit 10;"
if filter=="artist":
        query="SELECT * FROM songs WHERE " + searchby1 +  " LIKE '%" + search + "%';"
if filter=="title":
        query="SELECT * FROM songs WHERE " + searchby2 +  " LIKE '%" + search + "%';"
try:
    cursor.execute(query)
    #executes the query from above
except Exception as e:
    print(e)
    #if there is an error it will print an e
else:
    rows=cursor.fetchall()
    #will find all matches that match the query
    if rows==[]:
        print("No Result")
        #if no matches are found then it will print no result
    html = ""
    for row in rows:
            html += """
            <head>
            <style type="text/css">
            body{background-color:#D2FFF0;}
            h1{font-family:arial; font-size:40px;}
            p{font-family:arial; font-size:20px;}
            </style>
            </head>
            <img src='%s' />
            <h3>'%s'</h3>
            <p>'%s'</p>
            <p>'%s'</p>
            <p>'%s'</p>
            <hr>
            """ % (row[4], row[1], row[2], row[3], row[5])
    print(html)
    #if there is a match it will print the following html string

