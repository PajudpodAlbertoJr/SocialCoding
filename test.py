import ipaddress
def validate_ip_address(ip_string):
   try:
       ip_object = ipaddress.ip_address(ip_string)
       print(f"The IP address {ip_string} is valid.")
   except ValueError:
       print(f"The IP address {ip_string} is not valid")

validate_ip_address("127.0.0.1")

x = input()
print(x)
validate_ip_address(x)