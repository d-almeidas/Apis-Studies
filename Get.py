#Pegar informações do request

import requests
import json

req = requests.get('https://gorest.co.in/public/v2/users')
print(req.json())