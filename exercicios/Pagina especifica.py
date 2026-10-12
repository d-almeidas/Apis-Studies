import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GOREST_TOKEN")
url = "https://goarest.co.in/public/v2/users"
headers = {"Authorization": f"Bearer {token}"}

params = {"page": 2, "per_page": 5}

req = requests.get(url, headers=headers, timeout=10, params=params)

if req.ok: 
    print(req.status_code)
    usuarios=req.json()

    for pessoa in usuarios:
        print(f"ID: {pessoa["id"]}, NAME: {pessoa["name"]}")
else: 
    print("Erro:", req.status_code, req.text)