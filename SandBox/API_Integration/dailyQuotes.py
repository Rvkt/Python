import requests
import json

api_url = 'https://zenquotes.io/api/quotes'

response = requests.get(api_url)

quote = json.loads(response.text)

for i in range(len(quote)):
    print('Quote: ', quote[i]['q'])
    print('Author: ', quote[i]['a'])
    break
