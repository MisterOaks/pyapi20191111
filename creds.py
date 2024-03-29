#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    with open("/home/student/creds", "r") as mycreds:
        nasacreds = mycreds.read()
    
    nasacreds = "api_key=" + nasacreds.strip("\n")    
    apodresp = requests.get(NASAAPI + nasacreds)
    apod = apodresp.json()
    print(apod["title"])
    print(apod["date"])
    print(apod["explanation"])
    print(apod["url"])
if __name__ == "__main__":
    main()

