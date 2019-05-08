#!/usr/bin/env python3

import requests ## 3rd party URL lookup


## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2019-05-08' ## start date for data
    enddate = '&end_date=2019-05-08' ## create mechanism to utilize enddate
    mykey = '&api_key=BTXfSrFIjocZNzBAuRMSg5lQ9T6ONHulOdVPBWXb'  ## replace this with our API key

    neourl += startdate + mykey
    
    neojson = (requests.get(neourl)).json()

    print(neojson)
## call main

main()

