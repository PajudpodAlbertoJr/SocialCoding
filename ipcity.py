import requests
from requests import get

def ip_city():
    loc = (get('https://ipapi.co/json/').json())
    loc = loc['city']
    print (f"Your IP city location is: {loc}")