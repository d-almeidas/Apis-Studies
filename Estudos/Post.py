    #Cria informações do request

import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GOREST_TOKEN")
infos = {
    "name": "Amanda",
    "email": "Aman@example.com", 
    "gender": "Female",
    "status": "active",
}

headers = {"Authorization": f"Bearer {token}"}

req = requests.post('https://gorest.co.in/public/v2/users', json = infos, headers = headers)
print("Status Code:", req.status_code)
print(req.json())
