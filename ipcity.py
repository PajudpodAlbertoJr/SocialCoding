import requests
from requests import get

<<<<<<< HEAD
def ip_city():
    loc = (get('https://ipapi.co/json/').json())
    loc = loc['city']
    print (f"Your IP city location is: {loc}")
=======
#Gets the IP address city location from ipapi.co

def ip_city():
  loc = (get('https://ipapi.co/json/').json())
  loc = loc['city']
  print (f"Your IP city location is: {loc}")
>>>>>>> 2fbf131c45ce1b1133601f44afcb8873667e39b9
