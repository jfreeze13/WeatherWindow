#!/usr/bin/env python
#Author: Jessica Freeze

import sqlite3
import datetime
import hashlib
import cgi
import cgitb
cgitb.enable()

#insert new user into database
def insert_new_user(username,password):
    #make salt for hashing
    salt = str(datetime.datetime.now())

    #encode password and salt for hashlib use.
    password = password.encode('utf8')
    salt = salt.encode('utf8')

    #form the concatenation of hash and hash password + salt.
    hashing = hashlib.md5()
    hashing.update(password)
    hashing.update(salt)
    encrypt_pw = hashing.hexdigest()

    #connect to databse and establish a cursor
    conn = sqlite3.connect('weatherwindow.db')
    cursor = conn.cursor()

    #decode salt for putting into database and put into database
    salt = salt.decode('utf8')
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", [username,encrypt_pw,salt,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

    #commit changes to databse and close connection.
    conn.commit()
    conn.close()

#check if user exists in database already
def check_exists (username):
    conn = sqlite3.connect('weatherwindow.db')
    cursor = conn.cursor()

    #try to pull user given username from database
    result = cursor.execute("SELECT password FROM users WHERE username=?", [username])
    pw = cursor.fetchall()

    #return whether or not user was found in table.
    if pw != []:
        return True
    else:
        return False

#Pull user given info from input fields
login_form = cgi.FieldStorage()


#information about success or failure of sign up for user
print "Content-Type: text/html\n\n"
print 

#should never be seen by user but will be if not using html5.
if False:
    print '''<html>
                <head>
                    <title>Sign-Up Results</title>
                    <h1 id="Logout-header">
            			Please insert a Username and Password
            		</h1>
                </head>
                    <body>'''
    print '<META HTTP-EQUIV=refresh CONTENT=\"1;URL=/Login.html\">\n'

#checks if user exists using check exists function
else:
    #pulls user given data from forms
    username = login_form.getvalue('usernamefield')
    password = login_form.getvalue('passwordfield')

    #user account already exists in database
    if check_exists(username):
        print '<h1>User account', username, 'already exists. Please return to login page </h1>'
        #redirect to login page
        print '<META HTTP-EQUIV=refresh CONTENT=\"1;URL=/Login.html\">\n'
    #User not present in database yet, user saved into database
    else:
        insert_new_user(username, password)
        print '''<html>
            <head>
                <title>Sign-Up Results</title>
                <h1 id="Logout-header">
        			Your account has been created!
        		</h1>
            </head>
                <body>'''
        #redirect to mainscreen
        print '<META HTTP-EQUIV=refresh CONTENT=\"1;URL=/MainScreen.html\">\n'
        #print ("Location: login.html\n\n") #redirect to sign-up page



print '''
        </body>
    </html>'''
