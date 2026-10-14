import os 
import requests
from dotenv import load_dotenv
import time

load_dotenv()
token = os.getenv("GOREST_TOKEN")
url = "https://gorest.co.in/public/v2/usuarios"
headers = {"Authorization": f"Bearer {token}"}

lista_pessoas = []
pagina = 1

def get_with_retry(url, header=headers, tentativas=3, espera=2, **kwargs):
    for tentativa in range(1, tentativas + 1):
        try:
            req = requests.get(url, timeout=10, **kwargs)
            req.raise_for_status()
            return req
        
        except (requests.exceptions.Timeout,
                requests.exceptions.ConnectionError):
            print(f"Tentativa {tentativa}: falha de conexão.")

        except requests.exceptions.HTTPError as e:
            if e.response.status_code < 500:
                raise
            print(f"Tentativa {tentativa}: erro do servidor ({e.response.status_code}).")
            
        if tentativa <= tentativas:
            print('Testando...')
            time.sleep(espera)
            tentativa += 1
            continue

    raise Exception("A API não respondeu depois de várias tentativas.")

while pagina <= 3:
    params = {"page": pagina, "per_page": 20}
    req = get_with_retry(url, params=params)

    usuarios = req.json()
    pagina += 1 
    lista_pessoas.extend(usuarios) 
    print(f"Pagina atual: {pagina - 1}")
    
print(f"Todos os usuarios: {len(lista_pessoas)}")

