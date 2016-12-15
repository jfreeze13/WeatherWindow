#!/usr/bin/env python

#Author: Jessica Freeze
#Code very closely sourced to Robert St Jacque
#CSC210 Lecture 10 github repository

#Imports
import cgitb
import Cookie
import os
import cgi
import hashlib
import sqlite3
cgitb.enable()


#This function authenticates the password entered matches the password from the database for that username.
def authenticate(username,password):

    #A connection is established to the weather window database.
    conn = sqlite3.connect('weatherwindow.db')
    #A cursor for use in retrieving from the database is made.
    cursor = conn.cursor()

    #usernames matching the username entered by the user are requested from the users table in the weather window database.
    #Because username is a primary key, this will return only one name. Note the prepared statements to prevent sql injection.
    cursor.execute("SELECT username FROM users WHERE username=?", [username])
    user = cursor.fetchall()

    #checks to see if there was no user with that username yet created and returns a check value which is used to parse
    #an appropriate response.
    if user ==[]:
        return 1

    # pull from database the row with username matching what the user typed in and gets the password from that row.
    result = cursor.execute("SELECT password FROM users WHERE username=?", [username])
    pw=str(cursor.fetchone()[0])

    # pull from database the row with username matching what the user typed in and gets the salt from that row.
    #The salt is used to prevent password stealing.
    cursor.execute("SELECT salt FROM users WHERE username=?", [username])
    salt = str(cursor.fetchone()[0])

    #if user exists, take user given password and concatenate it with salt from database and then hash.
    if result.arraysize == 1:

        hashing = hashlib.md5()

        #encoding required by hashlib
        password = password.encode('utf-8')
        salt = salt.encode('utf-8')

        #concatenation function from hashlib
        hashing.update(password)
        hashing.update(salt)

        #hash concatenated string into encoding
        digest = hashing.hexdigest()

        #close database connection
        conn.close()

        #check if user hashed password matches database hashed password and returns check number.
        if digest==pw:
            return 2
        else:
            return 3
    else:
        return False


#pulls data from login fields populated by user.
login_form = cgi.FieldStorage()

#Code for handling user not filling in all fields should html5 autochecks not work
if "usernamefield" and "passwordfield" not in login_form:
    print 'Content-Type: text/html\n\n'
    print 
    print '''<html>
        <head>
            <title>Login Results</title>
        </head>
        <body>'''
    print '<h1>Please return to the login page and provide a username and password </h1>'
    print '''
        </body>
    </html>'''
elif "usernamefield"  not in login_form:
    print 'Content-Type: text/html\n\n'
    print 
    print '''<html>
        <head>
            <title>Login Results</title>
        </head>
        <body>'''
    print '<h1>Please return to the login page and provide a username</h1>'
    print '''
        </body>
    </html>'''
elif "passwordfield" not in login_form:
    print 'Content-Type: text/html\n\n'
    print 
    print '''<html>
        <head>
            <title>Login Results</title>
        </head>
        <body>'''
    print '<h1>Please return to the login page and provide a password </h1>'
    print '''
        </body>
    </html>'''
#If username and password both entered.
else:
    #extract username and password entered by user.
    username = login_form.getvalue('usernamefield')
    password = login_form.getvalue('passwordfield')

    #Create cookie with users given username and set expiration
    c = Cookie.SimpleCookie()
    c['username'] = username
    c['username']['path'] = '/'
    c['username']['expires'] = 30 * 24 * 60 * 60

    #Call authentication function above to check if password matches user password from database.
    pizza = authenticate(username,password)

    #check checkbits to determine response for logging in.
    #user successfully authenticated. Redirect to mainscreen.
    if pizza==2:
        #create cookie in browser
        print c
        print "Status: 301 Moved"
        print "Location:/MainScreen.html"
        print 
    #user authentication failed. redirect to failed login page
    elif pizza == 3:
        print "Status: 301 Moved"
        print "Location:/FailedLogin.html"
        print
    #user does not exist. redirect to failed login page.
    elif pizza ==1:
        print "Status: 301 Moved"
        print "Location:/FailedLogin.html"
        print
    #something random went wrong. Redirect to failed login page.
    else:
        print "Status: 301 Moved"
        print "Location:/FailedLogin.html"
        print 


