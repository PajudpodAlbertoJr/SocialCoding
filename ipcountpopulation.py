import requests
from requests import get

def population():
  loc = (get('https://ipapi.co/json/').json())
  loc = loc['country_population']
  print (f"Your IP country population is: {loc}")
