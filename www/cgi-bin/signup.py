#!"C:\Program Files (x86)\Ampps\python\python.exe"


#Code very closely sourced to Robert St Jacque
#CSC210 Lecture 10 github repository

#import _mysql
import sqlite3
import datetime
import hashlib
import cgi
import cgitb
cgitb.enable()


def insert_new_user(username,password):
    salt = str(datetime.datetime.now())

    password = password.encode('utf-8')
    salt = salt.encode('utf-8')
    hashing = hashlib.md5()
    hashing.update(password)
    hashing.update(salt)
    encrypt_pw = hashing.hexdigest()

    conn = sqlite3.connect('weatherwindow.db')
    cursor = conn.cursor()

    #Need to include here an error message if user already exists and double check
    #prepared statement

    cursor.execute("INSERT INTO users VALUES(?,?,?);", [username,encrypt_pw,salt])

    conn.commit()
    conn.close()

def check_exists (username):
    conn = sqlite3.connect('weatherwindow.db')
    cursor = conn.cursor()

    result = cursor.execute("SELECT * FROM users WHERE username=?", [username])
    if result.arraysize == 1:
        return True
    else:
        return False

login_form = cgi.FieldStorage()
print("Content-Type: text/html\n\n")
print ()

print ('''<html>
    <head>
        <title>Sign-Up Results</title>
    </head>
        <body>''')
if False:
    print ('<h1>Please insert a Username and Password </h1>')
    #figure out how to bring back to login page
else:
    username = login_form.getvalue('usernamefield')
    password = login_form.getvalue('passwordfield')

    if check_exists(username):
        print ('<h1>User account already exists. Please return to login page </h1>')
    else:
        insert_new_user(username, password)
        print ("Location: login.html\n\n")



print ('''
        </body>
    </html>''')