import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GOREST_TOKEN")
url = "https://gorest.co.in/public/v2/users"
headers = {"Authorization": f"Bearer {token}"}

req = requests.get(url, headers=headers, timeout=10)

if req.ok:
    usuarios = req.json()
    for pessoa in usuarios:
        print(f'ID:{pessoa["id"]}, NAME:{pessoa["name"]}, EMAIL:{pessoa["email"]}, STATUS:{pessoa["status"]}')
else:
    print("Erro:", req.status_code, req.text)