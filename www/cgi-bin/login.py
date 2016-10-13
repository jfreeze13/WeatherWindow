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

def create_database():
    conn = sqlite3.connect('weatherwindow.db')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS users')

    cursor.execute('CREATE TABLE IF NOT EXISTS users(username varchar(30) primary key, password varchar(200), salt charchar(100))')

    conn.commit()
    conn.close()

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

def user_check(): #Will include param for if new user or login access

    insert_new_user('tom', 'fancy')
    conn1 = sqlite3.connect('weatherwindow.db')
    cursor = conn1.cursor()
    for row in cursor.execute('SELECT * FROM users'):
        print (row)

    conn1.commit()
    conn1.close()

create_database()
user_check()

print("Content-Type: text/html\n\n")
print ()

print ('''<html>
    <head>
        <title>Login Results</title>
    </head>
        <body>
            Hello World! I am Jess''')


print ('''
        </body>
    </html>''')
