#!/usr/bin/python3
#Test script lifted from
# https://www.tutorialspoint.com/python3/python_database_access.htm
#tinkered with by plscks
# 'US' 'CA' OK
#
# Need to exclude local IPs from lists
#
#
#

import pymysql
import socket, struct
from geoip import geolite2

raw_ip = []
good_ip = []
bad_ip = []

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
    raw_ip.append(ip_src)

print(raw_ip)

#convert from integers to IPs
for i in raw_ip:
    ip = socket.inet_ntoa(struct.pack('!L', i))
    info = geolite2.lookup(ip)
    print(ip)
    infotest = info is None
    if infotest == False:
        if info.country == 'US' or info.country == 'CA':
            print(ip + ' Originates from ' + info.country + '. Added to good list')
            good_ip.append(ip)
        else:
            print(ip + ' Originates from ' + info.country + ' I don\'t trust this, added to bad list')
            bad_ip.append(ip)
    else:
        print('No info available, defaulting to bad list')
        print(ip + ' Added to bad list')

print('----------------GOOD LIST---------------------')
print(good_ip)
print()
print('----------------BAD  LIST---------------------')
print(bad_ip)
    
# Fetch a single row using fetchone() method.
#data = cursor.fetchone()

#print ("Database version : %s " % data)



# disconnect from server
db.close()
