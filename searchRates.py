#!/usr/bin/python3
# Nexus Clash search rates utility v0.2
# Written by plscks
# Utilizes WikiMedia built in api
# API documentation : https://wiki.nexuscla.sh/wiki/api.php
#
################
## TO DO LIST ##
################
# [X] get location page IDs in json format
# [X] sort page IDs into [locations: pageids]
# [X] get wikitext from pages by ID in json format
# [X] clean wiki text of useless information store in pageInfo =  [itemName: findWeight]
# [X] calculate search rate from findWeight totals
# [X] store in dictionary as locationRates = [itemName: searchRate]
# [] store in dictionary within dictionary masterRates = [itemName: [locationName: searchRate]]
# [] sort itemName by searchRate descending
# [] output as json to be imported in RRFBot
#
# Is this a test?
# It has to be.....
import json
import re
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

def getItemRates(location, pageid):
    """Gets item find weight from locations pages"""
    items = {}
    ## setup as {locationName: {itemName: findWeight}}
    response = requests.get('https://wiki.nexuscla.sh/wiki/api.php?action=parse&format=json&prop=wikitext&pageid=' + str(pageid))
    if response.status_code == 200:
        wikitext = json.loads(response.content.decode('utf-8'))
    else:
        print('Bad page ID, canceling request.')
    wikitext = wikitext['parse']['wikitext']['*']
    if 'Items found inside:' in wikitext:
        shortWikitext = wikitext[wikitext.find('|+ Items found inside:'):]
        insideFinds = shortWikitext.split('background-color:#f0f8ff;"', 1)[0]
        outsideFinds = wikitext[wikitext.find('|+ Items found outside:'):]
    else:
        shortWikitext = wikitext[wikitext.find('|+ Items found outside:'):]
        outsideFinds = shortWikiFinds
        insideFinds = None
##send text out to textParse() and set into lists
    if insideFinds == None:
        output = {}
        outsideItemNameList = textParse(outsideFinds)[0]
        outsideItemPercentList = textParse(outsideFinds)[1]
        tileNamePercent = dict(zip(outsideItemNameList, outsideItemPercentList))
        output['Outside ' + location] = tileNamePercent
        return output
    else:
        totalItemNameList = []
        totalItemPercentList = []
        output = {}
        insideItemNameList = textParse(insideFinds)[0]
        insideItemPercentList = textParse(insideFinds)[1]
        insideNamePercent = dict(zip(insideItemNameList, insideItemPercentList))
        outsideItemNameList = textParse(outsideFinds)[0]
        outsideItemPercentList = textParse(outsideFinds)[1]
        outsideNamePercent = dict(zip(outsideItemNameList, outsideItemPercentList))
        output['Inside ' + location] = insideNamePercent
        output['Outside ' + location] = outsideNamePercent
        return output

    items = dict(zip(insideItemNameList, insideItemRatePercent))
    print(items)

    return items

def textParse(text):
    itemNames = re.finditer(r'(?<=\[\[).+?(?=\])', text)
    itemNameList = []
    itemRateList = []
    for m in itemNames:
        intemNameList.append(m[0])
    itemRates = re.finditer(r'(?<=\| )\d', text)
    for m in itemRates:
        itemRateList.append(int(m[0]))
    itemRatePercent = weight2Rate(itemRateList)
    return itemNameList, itemRatePercent

def weight2Rate(inputWeights):
    """converts item find weight to search rates by percentage"""
    weightSum = sum(inputWeights)
    percentRates = []
    for i in inputWeights:
        percentRates.append((i / weightSum) * 100)
    return percentRates

if __name__ == "__main__":
    masterLocations = getCleanLocations()
    findRates = {}
    locationData = {}
    for k, v in masterLocations.items():
        LocationData[k] = getItemRates(k, v)[k]
        print('Key: ' + k + ' Value: ' + str(v))
