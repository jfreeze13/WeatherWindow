#!"C:\Program Files (x86)\Ampps\python\python.exe"
#!/usr/bin/env python
import cgitb

cgitb.enable()

import http.cookies as Cookie
import os

import cgi
login_form = cgi.FieldStorage()

#stored_cookie_string = os.environ.get('HTTP_COOKIE')
#c = Cookie.SimpleCookie(stored_cookie_string)

#nc = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
#nc['username'] = c['username']
#nc['username']['path'] = '/weatherwindow'
#nc['username']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'

<<<<<<< HEAD
nc = Cookie.SimpleCookie()
nc['username'] = c['username']
nc['username']['path'] = '/'
nc['username']['expires'] = "Thu, 01 Jan 1970 00:00:01 GMT:"
=======

>>>>>>> origin/master
print ('Content-Type: text/html')
#print (nc)
print ()
print ('<html>')
#print (c)
#print(nc)
#try:
 #   data = nc['username'].value
  #  print ('cookie data: ' , data , ' <br>')
#except KeyError:
 #   print ('The cookie was not set or has expired<br>')
print ('''<head>
		<title>Logout</title>
		<h1 id="Logout-header">
			You are logged out!
		</h1>
    "</body></html>"

	</head>
	<br><br>
	<body>
            <META HTTP-EQUIV=refresh CONTENT=\"1;URL=/Login.html\">
		</body>
</html>''')
print ()

