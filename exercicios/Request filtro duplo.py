import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GOREST_TOKEN")
url = "https://gorest.co.in/public/v2/users"
headers = {"Autohorization": f"Bearer {token}"}

params = {"gender":"female","status": "inactive"}

req = requests.get(url, headers=headers, timeout=10, params=params)
print(req.status_code)
print(req.url)

if req.ok:
    usuarios = req.json()
    for pessoa in usuarios:
        print(f'ID:{pessoa["id"]}, NAME:{pessoa["name"]}, STATUS:{pessoa["status"]}')