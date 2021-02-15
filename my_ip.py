import requests
from colorama import Fore, Back, Style 
# from termcolor import colored, cprint 

ip = requests.get("https://api.myip.com").json()

ip_num = ip["ip"]
ip_country = ip["country"]
ip_country_code = ip["cc"]

print('Your IP is :', ip_num) 
print('Your country is :', ip_country) 
print('Your country code is :', ip_country_code)
