#!/usr/bin/env python

# modified from St. Jacques' code

import cgitb
import cgi
import sqlite3

cgitb.enable()

login_form = cgi.FieldStorage()

print 'Content-Type: text/html'
print

print '''<html>
  <head>
    <title>Login Script</title>
    <style type="text/css">
      h1 {
          font-size: 25px;
          color: green;
      }
      .bluetext {
          color: blue;
      }
    </style>
  </head>
  <body>
'''

username = login_form['username'].value
password = login_form['password'].value
checkpassword = login_form['checkpassword'].value

#make sure password and checkpassword are equal before continuing

#if(password!=checkpassword){
#print 'Try Again'
#}


"""
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

c.execute('insert into accounts values (?,?,?)', (username, password, checkpassword))

conn.commit()
conn.close()
"""

print '<h1>You Are Logged In!'

print '<h2>Your username is: <span class="bluetext">' + username + '</span>'
print '<h2>Your password is: <span class="bluetext">' + password + '</span>'

print '''
  </body>
</html>
'''
