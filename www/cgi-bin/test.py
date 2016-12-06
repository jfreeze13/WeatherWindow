#!/usr/bin/env python

import cgitb
import cgi
import sqlite3
import json # used to send data back in JSON format

cgitb.enable() # enable debugging output in some cases

print "Content-type: application/json"
print # without printing a blank line, the "end of script output before headers" error will occur
#print("hello there!")
form = cgi.FieldStorage()

user = form['usernamefield'].value # don't forget the .value

conn = sqlite3.connect('weatherwindow.db')
cursor = conn.cursor()

data = {} # dictionary to store the response name/value pairs before JSON conversion

for username in cursor.execute("SELECT * FROM users WHERE username=?", [user]):

    data['name'] = order[0]

    print json.dumps(data)
