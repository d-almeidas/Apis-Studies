import os
import requests
from dotenv import load_dotenv

load_dotenv()
token=os.getenv("GOREST_TOKEN")
url= "https://gorest.co.in/public/v2/users"
headers= {"Authorization": f"Bearer {token}"}
nome_Desejado = "Amanda"

params = {"name": nome_Desejado}

req = requests.get(url, headers=headers, params=params, timeout=10)
print(req.status_code)
print(req.json())