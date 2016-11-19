#!"C:\Program Files (x86)\Ampps\python\python.exe"
# Lecture 08 - jQuery and Ajax

import cgitb
import cgi
import sqlite3
import json # used to send data back in JSON format

cgitb.enable() # enable debugging output in some cases

print "Content-type: application/json"
print # without printing a blank line, the "end of script output before headers" error will occur

form = cgi.FieldStorage()

customer_name = form['customer_name'].value # don't forget the .value

conn = sqlite3.connect('pizza_orders.db')
cursor = conn.cursor()

data = {} # dictionary to store the response name/value pairs before JSON conversion

for order in cursor.execute("SELECT * FROM pizza_orders WHERE name=?", [customer_name]):

    data['name'] = order[0]
    data['size'] = order[1]
    data['crust'] = order[2]
    data['toppings'] = order[3]
    data['phone'] = order[4]
    data['credit'] = order[5]

    print json.dumps(data)
