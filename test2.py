from requests import get


# def get_inf(x):
#     loc = get('https://ipapi.co/{x}/json/')
#     print (loc.json())
# get_inf('8.8.8.8')

def get_inf(x):
    loc = get(f'https://ipapi.co/{x}/json/')
    print(loc.json()['city'])
get_inf('8.8.8.8')