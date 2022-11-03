import requests 
from requests import get 

#import the request library


def ip_postal():
    loc = (get('https://ipapi.co/json/').json())
    loc = loc['postal']
    print (f"Your IP city postal is: {loc}")

def in_ip_postal(ip):
    loc = get(f'https://ipapi.co/{ip}/json/')
    loc = loc.json(['postal'])
    print(f'The postal location of IP, {ip} is: {loc}')


