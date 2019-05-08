#!/usr/bin/env python3

import urllib.request
import json
import webbrowser

# Define APOD
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=BTXfSrFIjocZNzBAuRMSg5lQ9T6ONHulOdVPBWXb' ## your key goes here


## Call the webservice
apodurlobj = urllib.request.urlopen(apodurl + mykey)

## read the file-like object
apodread = apodurlobj.read()

## decode json to python data structure
decodeapod = json.loads(apodread.decode('utf-8'))

## display our pythonic data
print("\n\nCoverted python data")
print(decodeapod)

## use firefox to open the HTTPS URL
input('\nPress Enter to open NASA Picture of the Day in Firefox')
webbrowser.open(decodeapod['url'])
