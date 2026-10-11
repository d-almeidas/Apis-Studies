#Para o código não quebrar quando a internet cai ou a API demora

import requests 
import os 
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GOREST_TOKEN")

url= "https://gorest.co.in/public/v2/users"
headers = {"Authorization": f"Bearer {token}"}

try:
    req = requests.get(url, headers=headers, timeout=10)
    if req.ok:
        usuarios = req.json()
        print(req.status_code)
        for pessoa in usuarios:
            print(f'ID:{pessoa["id"]}, NAME:{pessoa["name"]}, EMAIL:{pessoa["email"]}, STATUS:{pessoa["status"]}')
    req.raise_for_status()
    

except requests.exceptions.Timeout:
    print("A API demorou demais para responder.")
except requests.exceptions.ConnectionError:
    print("Sem conexão com a API.")
except requests.exceptions.HTTPError as e:
    print("A API devolveu um erro:", e)
except requests.exceptions.RequestException as e:
    print("Erro inesperado:", e)


