from urllib import response
import requests

url = 'https://www.okx.com'

data = '/api/v5/market/tickers?instType=SWAP'

response = requests.get(url+data)
print(response.json())
