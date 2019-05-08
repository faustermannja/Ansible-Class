#!/usr/bin/env python3


## yaml is NOT part of the standard library
## python3 -m install pyyaml
import yaml

def main():
    ## create a blob of data to work with
    hitchhikers = [{'name': 'Zaphod Beeblebrox', 'species': 'Betelgeusian'}, \
            {'name': 'Arthur Dent', 'species': 'Human'}]

    ## display our python data (a list containing two dictionaries)
    print(hitchhikers)

    ## create the yaml string
    yamlstring = yaml.dump(hitchhikers)

    # Display a single string of YAML
    print(yamlstring)

main()

