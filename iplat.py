from requests import get

loc = (get('https://ipapi.co/json/').json())
loc = loc['latitude']
print (f"Your IP city location is: {loc}")