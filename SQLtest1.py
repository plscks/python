#!/usr/bin/python3
# Test script lifted from
# https://www.tutorialspoint.com/python3/python_database_access.htm
# tinkered with (and then expanded on) by plscks
# 'US' 'CA' OK
#
# This program utilizes a file with known good IP addresses
# in the current directory, file name must be
# : IPlist.txt
#
# This is a functional program at this stage
#
# Need to:
# - remove debug info for production version
# - add check for sudo with message
# - add 'are you sure' message
# - add 'no foreign IPs detected' message
#

import iptc
import os
import pymysql
import socket, struct
from geoip import geolite2

raw_ip = []
good_ip = []
bad_ip = []
bad_intip = []
cwd = os.getcwd()
file = 'IPlist.txt'
fullFile = cwd + '/' + file

# Open database connection
db = pymysql.connect("localhost","python","python","snort" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# prepare sql inquiry
sql = 'select ip_src, count(*) from iphdr group by ip_src;'

# execute SQL query using execute() method.
cursor.execute(sql)

results = cursor.fetchall()
print(results)

# fetch IPs as raw int and load into list
for row in results:
    ip_src = row[0]
    raw_ip.append(ip_src)

print(raw_ip)
cursor.close()
db.close()

# convert from integers to IPs
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
        bad_ip.append(ip)

print('----------------GOOD LIST---------------------')
print(good_ip)
print()
print('----------------BAD  LIST---------------------')
print(bad_ip)


# Read known good IP's from file and remove them from bad_ip list
# - SUCCESS
goodList = open(fullFile,'r').read().split('\n')
goodList.pop()
print('----------KNOWN GOOD IP----------------------')
print(goodList)
bad_ip_final = [x for x in bad_ip if x not in goodList]
print('-----------BAD LIST FINAL--------------------')
print(bad_ip_final)

# Blacklist IP addresses in iptables
# - SUCCESS!
# Convert IPs to integers
# - SUCCESS
# Remove IPs from DB and commit
# - SUCCESS!!
for badip in bad_ip_final:
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
    rule = iptc.Rule()
    rule.src = badip
    target = iptc.Target(rule, 'DROP')
    rule.target = target
    chain.insert_rule(rule)
    print('blacklisted ' + badip + ' in iptables.')
    packedIP = socket.inet_aton(badip)
    badInt = struct.unpack('!L', packedIP)[0]
    bad_intip.append(badInt)
    print(badip + ' as an integer is ' + str(badInt))
    sqlDEL = 'delete from iphdr where ip_src=' + str(badInt) + ';'
    sqlDEL2 = 'delete from acid_event where ip_src=' + str(badInt) + ';'
    print(sqlDEL)
    print(sqlDEL2)
    db2 = pymysql.connect("localhost","python","python","snort" )
    cursor2 = db2.cursor()
    cursor2.execute(sqlDEL)
    cursor2.execute(sqlDEL2)
    results2 = cursor2.fetchall()
    print(results2)
    db2.commit()
    cursor2.close()
    db2.close()

print('List of IPs as integers to be removed from SQL database')
print(bad_intip)

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()

#print ("Database version : %s " % data)



# disconnect from server
#db.close()
