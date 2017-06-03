#!/usr/bin/python3
#Test script lifted from
# https://www.tutorialspoint.com/python3/python_database_access.htm
#tinkered with by plscks

import pymysql
import socket, struct

a = []

# Open database connection
db = pymysql.connect("localhost","python","python","snort" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

#prepare sql inquiry
sql = 'select ip_src, count(*) from iphdr group by ip_src;'

# execute SQL query using execute() method.
cursor.execute(sql)

results = cursor.fetchall()

#fetch IPs as raw int and load into list
for row in results:
    ip_src = row[0]
    a.append(ip_src)

print(a)

#convert from integers to IPs
for i in a:
    ip = socket.inet_ntoa(struct.pack('!L', i))
    print(ip) 
# Fetch a single row using fetchone() method.
#data = cursor.fetchone()

#print ("Database version : %s " % data)



# disconnect from server
db.close()
