from urllib import response
import requests
from requests import get

from requests import get

loc = (get('https://ipapi.co/json/').json())
print (loc['ip'])