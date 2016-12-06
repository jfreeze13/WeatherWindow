#!"C:\Program Files (x86)\Ampps\python\python.exe"
#!/usr/bin/env python

#Author: Jessica Freeze
#Code very closely sourced to Robert St Jacque
#CSC210 Lecture 10 github repository

#import _mysql
import cgitb
import http.cookies as Cookie
import os
import cgi
import hashlib
import sqlite3
cgitb.enable()


def authenticate(username,password):


    conn = sqlite3.connect('weatherwindow.db')
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
        #send cookie
        print (c)
        print ("Status: 301 Moved")
        print ("Location:/MainScreen.html")
        print ()

    elif pizza == 3:
        print ("Status: 301 Moved")
        print ("Location:/FailedLogin.html")
        print ()
    elif pizza ==1:
        print ("Status: 301 Moved")
        print ("Location:/FailedLogin.html")
        print ()
    else:
        print ("Status: 301 Moved")
        print ("Location:/FailedLogin.html")
        print ()


