import datetime
import os

past= datetime.date(2013, 1, 23)
date=past.strftime("%B %d, %Y was a %A")
print(date)


July= datetime.date(2011, 7,5)
March= datetime.date(2011, 3, 23)
time= July- March
print("The number of days between March 23, 2011 and July 5, 2011 is", time.days, "days")


file=os.path.basename("http://effbot.org/librarybook/datetime.txt")
print(file)
f= open("file.txt", "w")
f.write("This is a file created for Assignment 4")
f.close()


# a. SSH is a secure way to login into a server to create a path for communication between you and that server
# b. ls-l- This command lists all the files within the cwd with file details such as permission, size, and date modified
     # for example rwx------- 2 lestegem students 4096 Jan 24 12:56 t.py
                #  -rw------- 1 lestegem students 68 Feb 21 13:31 test.txt
    #ls*.py would return all files that en in ".py". for this example it would return
               # t.py
                #f.py
     
    # mkdir- this command creates directories. So if the command was mkdir i210, the directory i210 would be created
     #mv- This command is responsible for moving files it will also change its names
      #   mv t.py, test.py
     #cd- will take you back to the previous directory or the home directory. cd ./- will take you to the previous directory while cd ~ will take you all the way back to the home directory
      #   For example if we had called ls -l and then called cd ./ we would be taken back to the home directory
     #rm- This command will remove only files
     #    if I entered rm t.py it would remove t.py from the directory
      #   so the home directory would only have f.py, i211 and test.txt
       #  rm-r would remove an entire directory with all its contents
# c. chmod a+xr myfile.py- This commands gives everyone (user, group and other) access to execute and read myfile.py
          #      the resulting permission will be - rxr-xr-x
     #chmod u-x myfile.py- this command takes away the execution ability in myfile.py away from the user
     #           the resulting permission will be -rw-------
  #   chmod go-x myfile.py- this command takes away the execution ability in myfile away from the group and others
        #        the resulting permission will be -rw-------
      #chmod g +w myfile.py- this command gives the group access to wrtie to myfile.py
      #          the resulting permission will be -rw--w----
      #chmod 711 myfile.py- this command gives the user access to read, write and execute my file and the group and other access to execute myfile.py
       #         the resulting permission will be rwx--x--x
