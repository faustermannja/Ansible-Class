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
#print("\n\nConverted python data")
#print(helmetson)

people_in_space = []

for people in helmetson['people']:
 #   print(people)
    dict1 = {}
    dict1['first_name'] = people['name'].split(" ")[0]
    dict1['last_name'] = people['name'].split(" ")[1]
    dict1['craft'] = people['craft']
    people_in_space.append(dict1)
#print(people_in_space)
#yaml is NOT part of the standard library
#python3 -m pip install pyyaml
import yaml

## open a new file in write mode
zfile = open('people_in_space.yaml', 'w')

## use the yaml library
## USAGE: yaml.dump(input data, file like object)
## unlike json, the yaml lib uses .dump() to create YAML strings and write to files
## the json lib uses .dump() to create a string and .dumps() to write to files
yaml.dump(people_in_space, zfile)


## Display the file
## close the file when we are done
zfile.close()

yaml_file = open('people_in_space.yaml', 'r')
print(yaml_file.read())

