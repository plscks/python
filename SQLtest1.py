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
# - Add 'no foreign IPs detected' message
#
import sys

if (sys.version_info < (3, 0)):
    print('This program requires python 3.0 or greater.')
    print('Exiting.....')
    exit()

import iptc
import os
import pymysql
import socket, struct
from geoip import geolite2

dict = {}
raw_ip = []
good_ip = []
bad_ip = []
bad_intip = []
cwd = os.getcwd()
file = 'IPlist.txt'
fullFile = cwd + '/' + file

# Checking for root
if os.geteuid() != 0:
    exit("*** Elevated permissions are required\n*** Try again with sudo or as root.....")

# Compile list of raw integers from mySQL db
db = pymysql.connect("localhost","python","python","snort" )
cursor = db.cursor()
sql = 'select ip_src, count(*) from iphdr group by ip_src;'
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    ip_src = row[0]
    raw_ip.append(ip_src)
cursor.close()
db.close()

# convert from integers to IPs and check country of origin
for i in raw_ip:
    ip = socket.inet_ntoa(struct.pack('!L', i))
    info = geolite2.lookup(ip)
    infotest = info is None
    # Sometimes an IP with country = None makes it's way into the bad list and crashes line 88 with no value 
    if infotest == False:
        if info.country == 'US' or info.country == 'CA':
            good_ip.append(ip)
        else:
            bad_ip.append(ip)
            if info.country == None:          # Testing for no data failure
                dict[ip] = 'No county info'   # TEST
            else:
                dict[ip] = info.country
    else:
        bad_ip.append(ip)
        dict[ip] = 'No country info'
goodList = open(fullFile,'r').read().split('\n')
goodList.pop()
bad_ip_final = [x for x in bad_ip if x not in goodList]
# I don't know if this is proper or not, but it seems to work?
for temp in goodList:
    while True:
        try:
            dict.pop(temp)
        except KeyError:
            break

# Are you sure check
for ipbad in dict:
# Something happens right here sometimes if info.country is nothing at all.....
#    print(ipbad)
#    print(dict[ipbad])
    print(ipbad + ' from ' + dict[ipbad])
sure = input('Are you sure you want to blacklist these IPs? (Y/N): ').lower()
if sure in {'n', 'no', 'na', 'nope'}:
    print('Exiting with no changes applied')
    quit()

# Convert IPs to integers and remove from mySQL db
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
    sqlDEL = 'delete from iphdr where ip_src=' + str(badInt) + ';'
    sqlDEL2 = 'delete from acid_event where ip_src=' + str(badInt) + ';'
    db2 = pymysql.connect("localhost","python","python","snort" )
    cursor2 = db2.cursor()
    cursor2.execute(sqlDEL)
    cursor2.execute(sqlDEL2)
    results2 = cursor2.fetchall()
    db2.commit()
    cursor2.close()
    db2.close()
