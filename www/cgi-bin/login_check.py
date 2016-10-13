#!"C:\Program Files (x86)\Ampps\python\python.exe"


import cgitb
import cgi
import hashlib
import sqlite3
cgitb.enable()

def authenticate(username,password):
    conn = sqlite3.connect('weatherwindow')
    cursor = conn.cursor()

    result = conn.execute('SELECT * FROM users WHERE username=?', [username])
    if result.arraysize == 1:
        row = result.next()
        encrypt_pw = row[1]
        salt = row[2]

        hashing = hashlib.md5()
        hashing.update(password)
        hashing.update(salt)

        digest = hashing.hexidigest()



        return digest == encrypt_pw
    else:
        conn.close()
        return False



login_form = cgi.FieldStorage()

print ('Content-Type: text/html\n\n')
print ()

print ('''<html>
    <head>
        <title>Login Results</title>
    </head>
    <body>''')

#username = login_form['usernamefield'].value
#password = login_form['passwordfield'].value

username = {'username':'boy'}
password = {'password':'toy'}
if authenticate(username,password):
    print ('<h1>User ' + username + ' has been successfully authenticated!</h1>')
else:
    print ('<h1>Authentication Failed! </h1>')

print ('''
    </body>
</html>''')

