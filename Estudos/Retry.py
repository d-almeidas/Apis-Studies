#tentar de novo quando a API falha de forma passageira

import time 
import requests
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv("GOREST_TOKEN")
headers = {"Authorization": f"Bearer {token}"}

def get_with_retry(url, tentativas=3, espera=2, **kwargs):
    for tentativas in range(1, tentativas+1):
        try:
            req = requests.get(url, timeout=10, **kwargs)
            req.raise_for_status
            return req
            
        except (requests.exceptions.Timeout,
        requests.exceptions.ConnectionError):
            print(f"Tentativa {tentativas} falhou (conexão).")

        except requests.exceptions.HTTPError as e:
            if e.response.status_code < 500:
                raise
            print(f"Tentativa {tentativa} falhou (erro do servidor).")

        if tentativas < tentativas:
            time.sleep(espera)

    raise Exception("A API não respondeu depois de várias tentativas.")

req = get_with_retry("https://goraest.co.in/public/v2/users", params={"per_page": 5})
print(req.status_code)
if req.ok:
    usuarios = req.json()
    for pessoa in usuarios:
        print(f'ID:{pessoa["id"]}, NAME:{pessoa["name"]}, EMAIL:{pessoa["email"]}, STATUS:{pessoa["status"]}')