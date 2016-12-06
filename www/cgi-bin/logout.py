#!"C:\Program Files (x86)\Ampps\python\python.exe"
#!/usr/bin/env python
import cgitb

cgitb.enable()

import http.cookies as Cookie
import os
import json
import cgi
login_form = cgi.FieldStorage()

#stored_cookie_string = os.environ.get('HTTP_COOKIE')
#c = Cookie.SimpleCookie(stored_cookie_string)

#nc = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
#nc['username'] = c['username']
#nc['username']['path'] = '/weatherwindow'
#nc['username']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'


print ("Status: 301 Moved")
print ("Location:/Login.html")
print ()

