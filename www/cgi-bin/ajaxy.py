#!/usr/bin/env python

import cgi
import json

login_form = cgi.FieldStorage()
username = login_form.getvalue('usernamefield')
password = login_form.getvalue('passwordfield')
print 'Content-type: application/json'
print 
response={'username':username}
print json.JSONEncoder().encode(response)