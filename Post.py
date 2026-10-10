    #Cria informações do request

import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GOREST_TOKEN")
infos = {
    "name": "Daniel",
    "email": "danielexemplo_12342423@xample.com", 
    "gender": "male",
    "status": "active",
}

headers = {"Authorization": f"Bearer {token}"}

req = requests.post('https://gorest.co.in/public/v2/users', json = infos, headers = headers)
print("Status Code:", req.status_code)
print(req.json())
