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

cgitb.enable()

nc = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
username = nc['username'].value
presetNum = nc['presNum'].value
ssn = nc['ssn'].value
wthr = nc['wthr'].value
chck = nc['chk'].value
#print ("Status: 301 Moved")
#print ("Location:/MainScreen.html")
#print()
conn = sqlite3.connect('weatherwindow.db')
cursor = conn.cursor()
#print(presetNum)

if chck =='checked':
    if presetNum == '0':
        print(presetNum)
        print()
        cursor.execute("UPDATE users SET curback=?, curover=? WHERE username=?", (ssn,wthr,username))

    elif presetNum == '1':
        cursor.execute("UPDATE users SET back1=?, over1=? WHERE username=?", (ssn, wthr, username))
        print()
    elif presetNum == '2':
        print()
        cursor.execute("UPDATE users SET back2=?, over2=? WHERE username=?", (ssn, wthr, username))

    elif presetNum == '3':
        cursor.execute("UPDATE users SET back3=?, over3=? WHERE username=?", (ssn, wthr, username))
        print()
    elif presetNum == '4':

        cursor.execute("UPDATE users SET back4=?, over4=? WHERE username=?", (ssn, wthr, username))
        print()
    else:
        print("problem in update")
        print()


    #cursor.execute("SELECT curover FROM users WHERE username=?", [username])
    #user =str(cursor.fetchone()[0])
    #print(user)
    #print(presetNum)
    #print(ssn)
    #print(wthr)
    #print()

else:

    if presetNum == '1':
        #print(presetNum)
        cursor.execute("SELECT over1 FROM users WHERE username=?", [username])
        user = str(cursor.fetchone()[0])
        cursor.execute("SELECT back1 FROM users WHERE username=?", [username])
        userback = str(cursor.fetchone()[0])
        c = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
        c['ssn']['Path']='/'
        c['ssn']=userback
        c['wthr']['Path'] = '/'
        c['wthr'] = user
        print(c)
        print()
    elif presetNum == '2':
        cursor.execute("SELECT over2 FROM users WHERE username=?", [username])
        user = str(cursor.fetchone()[0])
        cursor.execute("SELECT back2 FROM users WHERE username=?", [username])
        userback = str(cursor.fetchone()[0])
        c2 = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
        c2['ssn']['Path'] = '/'
        c2['ssn'] = userback
        c2['wthr']['Path'] = '/'
        c2['wthr'] = user
        print(c2)
        print()
    elif presetNum == '3':
        cursor.execute("SELECT over3 FROM users WHERE username=?", [username])
        user = str(cursor.fetchone()[0])
        cursor.execute("SELECT back3 FROM users WHERE username=?", [username])
        userback = str(cursor.fetchone()[0])
        c3 = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
        c3['ssn']['Path'] = '/'
        c3['ssn'] = userback
        c3['wthr']['Path'] = '/'
        c3['wthr'] = user
        print(c3)
        print()
    elif presetNum == '4':
        cursor.execute("SELECT over4 FROM users WHERE username=?", [username])
        user = str(cursor.fetchone()[0])
        cursor.execute("SELECT back4 FROM users WHERE username=?", [username])
        userback = str(cursor.fetchone()[0])
        c4 = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
        c4['ssn']['Path'] = '/'
        c4['ssn'] = userback
        c4['wthr']['Path'] = '/'
        c4['wthr'] = user
        print(c4)
        print()
    else:
        print("problem in update")
        print()

conn.commit()
conn.close()
