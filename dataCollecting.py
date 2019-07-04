# Testing out collecting data from the NC profile API
# Here we go!
import requests

name = input('Name: ')
name.replace(' ', '%20')
response = requests.get('https://www.nexusclash.com/modules.php?name=Character&charname=' + str(name) + '&format=json')
data = response.json()
if data['result']['character']['id'] == 0:
    print('No character by that name')
    quit()
charClass = len(data['result']['character']['classes']) - 1
print('Character Name: ' + data['result']['character']['name']['name'])
print('Character ID: ' + str(data['result']['character']['id']))
print('Level: ' + str(data['result']['character']['level']))
print('Class: ' + data['result']['character']['classes'][charClass])
if data['result']['character']['status']['alive'] == True:
    print('Currently alive')
else:
    print('Currently floating above the planes')
