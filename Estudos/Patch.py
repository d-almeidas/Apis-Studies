    #Cria informações do request

import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GOREST_TOKEN")
infos = {
    "name": "João",
    "email": "JoJAO@example.com", 
    "gender": "male",
    "status": "active",
}

headers = {"Authorization": f"Bearer {token}"}

req = requests.patch('https://gorest.co.in/public/v2/users/8660631', json = infos, headers = headers)
print("Status Code:", req.status_code)
print(req.json())
