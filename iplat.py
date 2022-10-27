from requests import get

def ip_lat():
    loc = (get('https://ipapi.co/json/').json())
    loc = loc['latitude']
    print (f"Your IP latitude is: {loc}")