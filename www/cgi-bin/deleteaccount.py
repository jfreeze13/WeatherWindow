#!/usr/bin/env python
#!"C:\Program Files (x86)\Ampps\python\python.exe"

#Author: Jessica Freeze
#Code very closely sourced to Robert St Jacque
#CSC210 Lecture 10 github repository

#import _mysql
import sqlite3
import datetime
import hashlib
import cgi
import cgitb
import Cookie
import os
cgitb.enable()

def delete_user(username):

    conn = sqlite3.connect('weatherwindow.db')
    cursor = conn.cursor()

    #Need to include here an error message if user already exists and double check
    #prepared statement

    cursor.execute("DELETE FROM users WHERE username=?", [username])

    conn.commit()
    conn.close()

nc = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
username = nc['username'].value
delete_user(username)

print "Status: 301 Moved"
print "Location:/Login.html"
print


