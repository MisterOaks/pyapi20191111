#!/usr/bin/python3

import urllib.request
import json

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    '''reading json from the API'''
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    #strip off the attachment (JSON) and read it
    #the problem here is that it will read out as a string
    helmet = groundctrl.read()

    print(helmet)

    helmetson = json.loads(helmet.decode('utf-8'))

    print(type(helmet))
    print(type(helmetson))
    print(helmetson["number"])
    print(helmetson["people"])
    print(helmetson["people"][0])

    for astro in helmetson["people"]:
        print(astro["name"])



if __name__ == "__main__":
    main()


