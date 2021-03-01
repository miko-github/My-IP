import requests


ipObj = requests.get("https://api.myip.com").json()

ip, country, cc = ipObj

print('{\n\tip_address: {0},\n\tcountry: {1},\n\tcountry_code: {2}\n}'.format(ip,county,cc))

# ip_num = ip["ip"]
# ip_country = ip["country"]
# ip_country_code = ip["cc"]

# print('Your IP is :', ip_num) 
# print('Your country is :', ip_country) 
# print('Your country code is :', ip_country_code)
