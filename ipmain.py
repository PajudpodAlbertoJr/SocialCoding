from stringprep import in_table_a1
from IPAPI import my_ip
from ipcity import ip_city, in_ip_city
from iplat import ip_lat
from ipcountarea import c_area
from ippostal import postal
from ipcountpopulation import population

import ipaddress
def validate_ip_address(ip_string):
   try:
       ip_object = ipaddress.ip_address(ip_string)
       print(f"The IP address {ip_string} is valid.")

       return True
   except ValueError:
       print(f"The IP address {ip_string} is not valid", end = " ")

       return False

#validate_ip_address("127.0.0.1")

def show_details():
    my_ip()
    ip_city()
    ip_lat()
    c_area()
    postal()
    population()

while 1:

    print('Welcome to IP App')
    print('Select a Process:')
    print('a: Show your IP Address Details')
    print('b: Show IP details of a certain IP Address')

    user_in = input('Any key except a and b to quit: ')

    if user_in == "a":
        show_details()
    
    elif user_in == "b":
        while 1:
            ip_in = input('Please enter an IP Address: \n')
            if validate_ip_address(ip_in) == True:
                in_ip_city(ip_in)
                break
            else:
                print(', please input a valid IP Address')
    else:
        break