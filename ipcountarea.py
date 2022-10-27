from requests import get

loc = (get('https://ipapi.co/json/').json())
loc = loc['country_area']
print (f"Your IP country area is: {loc}")
