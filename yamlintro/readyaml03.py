#!/usr/bin/env python3


import yaml
def main():
    ##Open a blob of YAML data
    yammyfile = open('/home/student/Ansible-Class/yamlintro/myYAML.yml', 'r')

    ## convert YAML into python data structures (lists and dictionaries)
    pyyammy = yaml.load(yammyfile)


    # display our new python data
    print(pyyammy)
    
main()
