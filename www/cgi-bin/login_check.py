#!"C:\Program Files (x86)\Ampps\python\python.exe"


import cgitb
import cgi
import hashlib
import sqlite3
cgitb.enable()

def authenticate(username,password):
    conn = sqlite3.connect('weatherwindow.db')
    cursor = conn.cursor()

    result = cursor.execute("SELECT * FROM users")# WHERE username=?", [username])
    return result
    #if result.arraysize == 1:

     #   row = result.next()
      #  encrypt_pw = row[1]
       # salt = row[2]

        #hashing = hashlib.md5()
        #hashing.update(password)
        #hashing.update(salt)

        #digest = hashing.hexidigest()



        #return digest == encrypt_pw
    #else:
    conn.close()
       # return False





login_form = cgi.FieldStorage()

print ('Content-Type: text/html\n\n')
print ()

print ('''<html>
    <head>
        <title>Login Results</title>
    </head>
    <body>''')

if "usernamefield" not in login_form:
    print ('<h1>We gotta problem kids </h1>')
username = login_form.getvalue('usernamefield')
password = login_form.getvalue('passwordfield')

result = authenticate(username,password)

if result:
    print ('<h1>User ' , username , ' has been successfully authenticated!</h1>')
else:
    print ('<h1>Authentication Failed! </h1>')


print ('''
    </body>
</html>''')

