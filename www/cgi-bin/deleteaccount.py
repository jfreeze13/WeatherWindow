#!/usr/bin/env python
#!"C:\Program Files (x86)\Ampps\python\python.exe"

#Author: Jessica Freeze

import sqlite3
import Cookie
import os

def delete_user(username):

    #Connect to databse and create a cursor for movement in db
    conn = sqlite3.connect('weatherwindow.db')
    cursor = conn.cursor()

    #delete row with given username from database. Because username is the primary key, this deletes the user.
    cursor.execute("DELETE FROM users WHERE username=?", [username])

    #commits the database changes and closes the connection so we don't overload ports.
    conn.commit()
    conn.close()

#Pull cookie which contains name of current user.
nc = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
#Call function to delete user with username found in cookie
delete_user(nc['username'].value)

#make it so page auto redirects to login page when this script is called instead of python page.
print "Status: 301 Moved"
print "Location:/Login.html"
print
