#!"C:\Program Files (x86)\Ampps\python\python.exe"
#Author: Jessica Freeze
#CS code sourced highly from Professor Robert St. Jacque
#CSC210 Lecture 10 github repository

#Import stuff
#sqlite3 used for ease of versioning over Mysql
import cgitb
import cgi
import hashlib
import sqlite3
cgitb.enable()

#authenticate that this user's password and username match what is present in the database
def authenticate(username,password):
    conn = sqlite3.connect('weatherwindow.db')
    #conn.row_factory = lambda cursor, row: row[0]
    cursor = conn.cursor()

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

        return digest==pw
    else:

        return False





login_form = cgi.FieldStorage()

print ('Content-Type: text/html\n\n')
print ()

print ('''<html>
    <head>
        <title>Login Results</title>
    </head>
    <body>''')

if "usernamefield" and "passwordfield" not in login_form:
    print ('<h1>Please return to the login page and provide a username and password </h1>')
elif "usernamefield"  not in login_form:
    print ('<h1>Please return to the login page and provide a username</h1>')
elif "passwordfield" not in login_form:
    print ('<h1>Please return to the login page and provide a password </h1>')
else:
    username = login_form.getvalue('usernamefield')
    password = login_form.getvalue('passwordfield')

    pizza = authenticate(username,password)


#print('<h1> output', pizza,' </h1>')

    if pizza:
        print ('<h1>User ' , username , ' has been successfully authenticated!</h1>')
    else:
        print ('<h1>Authentication Failed for username', username, '! </h1>')


print ('''
    </body>
</html>''')

