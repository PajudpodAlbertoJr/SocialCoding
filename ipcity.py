import requests
from requests import get

#Gets the IP address city location from ipapi.co

def ip_city():
  loc = (get('https://ipapi.co/json/').json())
  loc = loc['city']
  print (f"Your IP city location is: {loc}")

def in_ip_city(ip):
  loc = get(f'https://ipapi.co/{ip}/json/')
  loc = loc.json()['city']
  print(f'The city location of IP address, {ip}, is {loc}')