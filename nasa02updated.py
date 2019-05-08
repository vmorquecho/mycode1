#!/usr/bin/env python3

import requests

def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?
    startdate =
    endate = '&end_date=END_DATE'
    mykey = '&api_key=DEMO_KEY'

    neourl += startdate + mykey

    neojson = (request.get(neourl)).json()

    print(neojson)

main()
