#!/usr/bin/python3
import time # we need this for the sleep function
from datetime import datetime # required to use datetime.datetime.now()

def main():
    startTime = datetime.now()    # returns the time of right now from the datetime object
    # Note that datetime is an object, not a simple string.
    ## WRITE YOUR OWN CODE TO DO SOMETHING. ANYTHING.
    # SUGGESTION: Replace with code to print a question to screen and collect data from user.
    # MORE DIFFICULT -- Place the response(s) \
    # in a list & continue asking the question until the user enters the word 'quit'


    ## Explore the startTime object
    print('The startTime hour is:', startTime.hour)
    print('The startTime minute is:', startTime.minute)
    print('The startTime day is:', startTime.day)
    print('The startTime year is:', startTime.year)

    ## put the program to sleep for two seconds
    time.sleep(2)

    ## Figure out how long it took to do that something
    print('The code took:', datetime.now() - startTime, 'to run.')

    # Age

    age = datetime(1995, 4, 16, 12, 20, 35)

    print(age)

    timenow = datetime.now()

    latest = timenow - age
    print(latest.seconds)

if __name__ == '__main__':
    main()

