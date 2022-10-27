from requests import get

loc = (get('https://ipapi.co/json/').json())
loc = loc['postal']

print (f"Your IP city postal is: {loc}")
