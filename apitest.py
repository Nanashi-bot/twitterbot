import requests

url = "https://stoic.tekloon.net/stoic-quote"
stoic_quote = requests.request("GET", url).json()['data']['quote']
print(stoic_quote)
