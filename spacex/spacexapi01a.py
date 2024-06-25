#!/usr/bin/python3
"""
Author: RZFeeser
This program harvests SpaceX data avail from
https://api.spacexdata.com/v3/cores using the
Python Standard Library methods
"""

# using std library method for getting at API data

import urllib.request as rs
import json

# GLOBAL / CONSTANT of the API we want to lookup

SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():
     # create a urllib.request response object by sending an HTTP GET to SPACEXURI
    coreData = rs.urlopen(SPACEXURI)

    # pull STRING data off of the 200 response (even though it's JSON!)
    xstring = coreData.read().decode()
    print(type(xstring))

    # convert STRING data into Python Lists and Dictionaries
    listOfCores = json.loads(xstring)
    print(type(listOfCores))

    for core in listOfCores:
        print(core, end="\n\n")


if __name__ == "__main__":
    main()
