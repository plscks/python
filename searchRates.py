#!/usr/bin/python3
# Nexus Clash search rates utility v0.1
# Written by plscks
# Utilizes WikiMedia built in api
# API documentation : https://wiki.nexuscla.sh/wiki/api.php
#
################
## TO DO LIST ##
################
# [X] get location page IDs in json format
# [X] sort page IDs into [locations: pageids]
# [] get wikitext from pages by ID in json format
# [] clean wiki text of useless information store in pageInfo =  [itemName: findWeight]
# [] calculate search rate from findWeight totals
# [] store in dictionary as locationRates = [itemName: searchRate]
# [] store in dictionary within dictionary masterRates = [itemName: [locationName: searchRate]]
# [] sort itemName by searchRate descending
# [] output as json to be imported in RRFBot
#
# Is this a test?
# It has to be.....
import json
import requests

def getRawLocations():
    """Gets json data of all current breath locations wiki page ids"""
    response = requests.get('https://wiki.nexuscla.sh/wiki/api.php?action=query&list=categorymembers&cmtitle=Category:Current%20Locations&cmlimit=max&format=json')
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def getCleanLocations():
    """Sorts current breath locations into single dictionary {'Tile name': 'pageid'}"""
    locations = getRawLocations()
    masterLocation = {}
    for i in locations['query']['categorymembers']:
        masterLocation[i['title']] = i['pageid']
    return masterLocation

def getRates(masterLocations):
    """Gets item find weight from locations pages"""

def weight2Rate():
    """converts item find weight to search rates by percentage"""

if __name__ == "__main__":
    masterLocations = getCleanLocations()
    print(masterLocations)
