# check to see how many listeners on the icecast server
# written by plscks
import RPi.GPIO as GPIO
import urllib.request


response = urllib.request.urlopen('http://localhost:8001')
html = response.read()
test = str(html)
linenumber = test.find("Listeners (current)")
streamnumber = linenumber + 49
listenernumber = test[streamnumber]
#print(test)
print('There is(are) currently ' + str(listenernumber) + ' listener(s) on the icecast server.')
if int(listenernumber) > 0:
    print('there are listeners')
else:
    print('there are no listeners')
