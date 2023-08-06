import random
import requests

random.seed(20)
print(random.seed(20))

random_number = random.randint(0, 10)
print(random_number)

import requests

url = 'https://www.random.org/integers/?num=1&min=0&max=100&col=5&base=10&format=plain&rnd=new'

number = requests.get(url)

print(number)
print(int(number.text))

import requests

response = requests.get('https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint16')
print(response.text)

data = response.json()
random_int = data['data'][0]
print(random_int)