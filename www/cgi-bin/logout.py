#!/usr/bin/env python
import cgitb

cgitb.enable()

import Cookie
import os

import cgi
login_form = cgi.FieldStorage()

stored_cookie_string = os.environ.get('HTTP_COOKIE')
c = Cookie.SimpleCookie(stored_cookie_string)

nc = Cookie.SimpleCookie()
nc['username'] = c['username']
nc['username']['path'] = '/'
nc['username']['expires'] = -1 * 30 * 24 * 60 * 60

print ('Content-Type: text/html')
print nc
print
print ('<html>')
try:
    data = c['username'].value
    print ('cookie data: ' , data , ' <br>')
except KeyError:
    print ('The cookie was not set or has expired<br>')
print ('''<head>
		<title>Logout</title>
		<h1 id="Logout-header">
			You are logged out!
		</h1>
    "</body></html>"

	</head>
	<br><br>
	<body>
            <META HTTP-EQUIV=refresh CONTENT=\"1;URL=/MainScreen.html\">
		</body>
</html> ''')
print
