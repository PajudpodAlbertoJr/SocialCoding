import requests
from requests import get

def c_area():
  #get location of an IP address from ipapi.co 
  loc = (get('https://ipapi.co/json/').json())
  #input a parameter, country_area is the parameter here
  loc = loc['country_area']
  print (f"Your IP country area is: {loc}")

def in_c_area(ip):
  loc = get(f'https://ipapi.co/{ip}/json/')
  loc = loc.json()['country_area']
  print(f'The country area of IP Address, {ip}, is: {loc}')
