import urllib.request
import json
## Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'

## Call the webservice
groundctrl = urllib.request.urlopen(majortom)

## Put fileobject into helmet
helmet = groundctrl.read()

## Decode json to python data structure
helmetson = json.loads(helmet.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(helmetson)

print("\n\nPeople in Space: ", helmetson['number'])
people = helmetson['people']
print(people)