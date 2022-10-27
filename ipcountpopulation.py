#The code was imported from ipapi.co which displays the population of a specific country.

import requests
from requests import get

def population():
  loc = (get('https://ipapi.co/json/').json())
  loc = loc['country_population']
  print (f"Your IP country population is: {loc}")
