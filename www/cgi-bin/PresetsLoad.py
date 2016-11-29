#!"C:\Program Files (x86)\Ampps\python\python.exe"
# #!/usr/bin/env python

#Author: Jessica Freeze

#Import stuff
#sqlite3 used for ease of versioning over Mysql
import cgitb
import http.cookies as Cookie
import os
import cgi
import hashlib
import sqlite3

nc = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
username = nc['username'].value
presetNum = nc['presNum'].value

#print ("Status: 301 Moved")
#print ("Location:/MainScreen.html")
print ()
conn = sqlite3.connect('weatherwindow.db')
cursor = conn.cursor()
print(presetNum)
if presetNum == '1':
    print(presetNum)
    cursor.execute("SELECT over1 FROM users WHERE username=?", [username])
    user = str(cursor.fetchone()[0])
elif presetNum == '2':
    print(presetNum)
    cursor.execute("UPDATE users SET back2=?, over2=? WHERE username=?", (ssn, wthr, username))
    print(presetNum)
elif presetNum == '3':
    print(presetNum)
    cursor.execute("UPDATE users SET back3=?, over3=? WHERE username=?", (ssn, wthr, username))
    print(presetNum)
elif presetNum == '4':
    print(presetNum)
    cursor.execute("UPDATE users SET back4=?, over4=? WHERE username=?", (ssn, wthr, username))
    print(presetNum)
else:
    print("problem in update")


print(user)
print(presetNum)
print()

conn.commit()
conn.close()