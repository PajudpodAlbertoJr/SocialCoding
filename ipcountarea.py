from requests import get

def c_area():
  loc = (get('https://ipapi.co/json/').json())
  loc = loc['country_area']
  print (f"Your IP country area is: {loc}")
