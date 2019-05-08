#!/usr/bin/env python3



import urllib.request
import json

## Define NEOapi
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2019-05-08'
enddate = '&end_date=2019-05-08'
mykey = '&api_key=BTXfSrFIjocZNzBAuRMSg5lQ9T6ONHulOdVPBWXb' ## your key goes in here

neourl += startdate + mykey

## call the webservice
neourlobj = urllib.request.urlopen(neourl)


## read the file-like object
neoread = neourlobj.read()

## decode json to python data structure
decodeneo = json.loads(neoread.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(decodeneo)



