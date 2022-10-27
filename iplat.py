from requests import get

#Gets the IP address latitude coordinate

def ip_lat():
  loc = (get('https://ipapi.co/json/').json())
  loc = loc['latitude']
  print (f"Your IP city location is: {loc}")
