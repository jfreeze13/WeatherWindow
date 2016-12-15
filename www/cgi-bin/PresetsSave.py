#!/usr/bin/env python

#Author: Jessica Freeze

#Import stuff
#sqlite3 used for ease of versioning over Mysql
import cgitb
import Cookie
import os
import cgi
import hashlib
import sqlite3

#enable useful error messages
cgitb.enable()


#pull cookie values to get current window settings and user info
nc = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
username = nc['username'].value
presetNum = nc['presNum'].value
ssn = nc['ssn'].value
wthr = nc['wthr'].value
chck = nc['chk'].value

#connect to database and make cursor for database movement
conn = sqlite3.connect('weatherwindow.db')
cursor = conn.cursor()

#If user has indicated that they would like to update presets
if chck =='checked':
    #determine which preset button was clicked
    if presetNum == '0':
        #background debugging code not seen by user. Checks that current backgrounds are able to be saved porpoerly.
        print presetNum
        print
        cursor.execute("UPDATE users SET curback=?, curover=? WHERE username=?", (ssn,wthr,username))

    #save current background to the preset in database
    elif presetNum == '1':
        cursor.execute("UPDATE users SET back1=?, over1=? WHERE username=?", (ssn, wthr, username))
        print
    elif presetNum == '2':
        print
        cursor.execute("UPDATE users SET back2=?, over2=? WHERE username=?", (ssn, wthr, username))
    elif presetNum == '3':
        cursor.execute("UPDATE users SET back3=?, over3=? WHERE username=?", (ssn, wthr, username))
        print
    elif presetNum == '4':
        cursor.execute("UPDATE users SET back4=?, over4=? WHERE username=?", (ssn, wthr, username))
        print
    else:
        print "problem in update"
        print

#if user would like to pull up a preset.
else:

    #pull background and weather overlay from database preset selected and overwrite cookies to these values
    if presetNum == '1':
        cursor.execute("SELECT over1 FROM users WHERE username=?", [username])
        user = str(cursor.fetchone()[0])
        cursor.execute("SELECT back1 FROM users WHERE username=?", [username])
        userback = str(cursor.fetchone()[0])
        c = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
        c['ssn']['Path']='/'
        c['ssn']=userback
        c['wthr']['Path'] = '/'
        c['wthr'] = user
        c['username']['Path'] = '/'
        c['username'] = username
        c['presNum']['Path'] = '/'
        c['presNum'] = presetNum
        c['chk']['Path'] = '/'
        c['chk'] = chck
        print c
        print
    elif presetNum == '2':
        cursor.execute("SELECT over2 FROM users WHERE username=?", [username])
        user = str(cursor.fetchone()[0])
        cursor.execute("SELECT back2 FROM users WHERE username=?", [username])
        userback = str(cursor.fetchone()[0])
        c2 = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
        c2['ssn']['Path'] = '/'
        c2['ssn'] =userback
        c2['wthr']['Path'] = '/'
        c2['wthr'] =user
        c2['username']['Path'] = '/'
        c2['username'] = username
        c2['presNum']['Path'] = '/'
        c2['presNum'] = presetNum
        c2['chk']['Path'] = '/'
        c2['chk'] = chck
        print c2
        print
    elif presetNum == '3':
        cursor.execute("SELECT over3 FROM users WHERE username=?", [username])
        user = str(cursor.fetchone()[0])
        cursor.execute("SELECT back3 FROM users WHERE username=?", [username])
        userback = str(cursor.fetchone()[0])
        c3 = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
        c3['ssn']['Path'] = '/'
        c3['ssn'] =userback
        c3['wthr']['Path'] = '/'
        c3['wthr'] =user
        c3['username']['Path'] = '/'
        c3['username'] = username
        c3['presNum']['Path'] = '/'
        c3['presNum'] = presetNum
        c3['chk']['Path'] = '/'
        c3['chk'] = chck
        print c3
        print 
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
        c4['username']['Path'] = '/'
        c4['username'] = username
        c4['presNum']['Path'] = '/'
        c4['presNum'] = presetNum
        c4['chk']['Path'] = '/'
        c4['chk'] = chck
        print c4
        print 
    else:
        print "problem in update"
        print 

#commit databse changes and close connection
conn.commit()
conn.close()
