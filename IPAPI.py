from urllib import response
import requests
from requests import get

loc = (get('https://ipapi.co/json/').json())
loc = loc['ip']
print (f"Your public IP is: {loc}")

