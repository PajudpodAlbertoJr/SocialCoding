from requests import get

def postal():
  loc = (get('https://ipapi.co/json/').json())
  loc = loc['postal']

  print (f"Your IP city postal is: {loc}")
