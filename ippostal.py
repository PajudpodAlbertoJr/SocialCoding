from requests import get 

#gets the IP add city postal from ipapi.co

def postal():
  loc = (get('https://ipapi.co/json/').json())
  loc = loc['postal']

  print (f"Your IP city postal is: {loc}")
