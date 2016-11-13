#!/usr/bin/env python
#!"C:\Program Files (x86)\Ampps\python\python.exe"
#Author: Jessica Freeze
#CS code sourced highly from Professor Robert St. Jacque
#CSC210 Lecture 10 github repository

#Import stuff
#sqlite3 used for ease of versioning over Mysql
import cgitb

cgitb.enable()

#authenticate that this user's password and username match what is present in the database
def authenticate(username,password):
    import hashlib
    import sqlite3

    conn = sqlite3.connect('weatherwindow.db')
    #conn.row_factory = lambda cursor, row: row[0]
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE username=?", [username])
    user = cursor.fetchall()
    if user ==[]:
        return 1
    #pull from database the row with username matching what the user typed in.
    result = cursor.execute("SELECT password FROM users WHERE username=?", [username])
    pw=str(cursor.fetchone()[0])


    cursor.execute("SELECT salt FROM users WHERE username=?", [username])
    salt = str(cursor.fetchone()[0])


    if result.arraysize == 1:

        hashing = hashlib.md5()
        #password = str(password)

        password = password.encode('utf-8')
        salt = salt.encode('utf-8')

        hashing.update(password)
        hashing.update(salt)



        digest = hashing.hexdigest()
        conn.close()

        if digest==pw:
            return 2
        else:
            return 3
    else:

        return False

import Cookie
import os

import cgi
login_form = cgi.FieldStorage()

if "usernamefield" and "passwordfield" not in login_form:
    print ('Content-Type: text/html\n\n')
    print ()
    print ('''<html>
        <head>
            <title>Login Results</title>
        </head>
        <body>''')
    print ('<h1>Please return to the login page and provide a username and password </h1>')
    print ('''
        </body>
    </html>''')
elif "usernamefield"  not in login_form:
    print ('Content-Type: text/html\n\n')
    print ()
    print ('''<html>
        <head>
            <title>Login Results</title>
        </head>
        <body>''')
    print ('<h1>Please return to the login page and provide a username</h1>')
    print ('''
        </body>
    </html>''')
elif "passwordfield" not in login_form:
    print ('Content-Type: text/html\n\n')
    print ()
    print ('''<html>
        <head>
            <title>Login Results</title>
        </head>
        <body>''')
    print ('<h1>Please return to the login page and provide a password </h1>')
    print ('''
        </body>
    </html>''')
else:
    username = login_form.getvalue('usernamefield')
    password = login_form.getvalue('passwordfield')

    #Create cookie
    c = Cookie.SimpleCookie()
    c['username'] = username
    c['username']['path'] = '/'
    c['username']['expires'] = 30 * 24 * 60 * 60

    pizza = authenticate(username,password)

    #print('<h1> output', pizza,' </h1>')

    if pizza==2:
        print "Content-Type: text/html"
        #send cookie
        print c
        print
        print ('<h1>User ' , username , ' has been successfully authenticated!</h1>')
        #redirect to welcome page
        print '<META HTTP-EQUIV=refresh CONTENT=\"1;URL=/MainScreen.html\">\n'
        print
        print ('''
            </body>
        </html>''')
    elif pizza == 3:
        print "Content-Type: text/html"
        print
        print ('<h1>Authentication Failed for username', username, '! </h1>')
        print '<META HTTP-EQUIV=refresh CONTENT=\"1;URL=/FailedLogin.html\">\n'
        print
        print ('''
            </body>
        </html>''')
    elif pizza ==1:
        print "Content-Type: text/html"
        print
        print ('<h1>No such username', username, 'exists. Please go to signup page. </h1>')
        print '<META HTTP-EQUIV=refresh CONTENT=\"1;URL=/FailedLogin.html\">\n'
        print ('''
            </body>
        </html>''')
    else:
        print "Content-Type: text/html"
        print
        print ('<h1>What happened?! </h1>')
        print '<META HTTP-EQUIV=refresh CONTENT=\"1;URL=/FailedLogin.html\">\n'
        print ('''
            </body>
        </html>''')
