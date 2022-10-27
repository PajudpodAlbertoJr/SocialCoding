from urllib import response
import requests
from requests import get

#Identifies the IP address of the user

def my_ip():
    loc = (get('https://ipapi.co/json/').json())
    loc = loc['ip']
    print (f"Your public IP is: {loc}")

