#!/usr/bin/env python3


#yaml is NOT part of the standard library
#python3 -m pip install pyyaml
import yaml

def main():
    ## create a blob of data to work with
    hitchhikers = [{'name' : 'Zaphod Beeblebox', "species": 'Betelgeusian'}, \
            {'name': 'Arthur Dent', "species": 'Human'}]
    print(yaml.dump(hitchhikers))
    ## display our python data (a list containing two dictionaries)
    print(hitchhikers)

    ## open a new file in write mode
    zfile = open('galaxyguide.yaml', 'w')

    ## use the yaml library
    ## USAGE: yaml.dump(input data, file like object)
    ## unlike json, the yaml lib uses .dump() to create YAML strings and write to files
    ## the json lib uses .dump() to create a string and .dumps() to write to files
    yaml.dump(hitchhikers, zfile)

    ## close the file when we are done
    zfile.close()

main()

