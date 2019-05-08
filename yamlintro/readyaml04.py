#!/usr/bin/env python3

#yaml is NOT part of the standard library
#python3 -m pip install pyyaml
import yaml


def main():
    ## Open a blob of YAML data
    yammyfile = open('/home/student/Ansible-Class/yamlintro/myYAML.yml', 'r')

    ## pull in yaml as python lists and dictionaries
    pyyammy = yaml.load(yammyfile)

    ## close our open file object
    yammyfile.close()

    ## how does our data currently look?
    print(pyyammy)

    ## add minecraft to the list of apps
    pyyammy[0]['apps'].append('minecraft')


    ## Did the python data change?
    print(pyyammy)

    ## open a file to dump out to
    yammyfile2 = open('/home/student/Ansible-Class/yamlintro/myYAML.yaml.updated', 'w')

    ## use the yaml library
    ## USAGE: yaml.dump(input data, file like object)
    yaml.dump(pyyammy, yammyfile2)

    ## close our file
    yammyfile2.close()
   
main()
