import os 
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GOREST_TOKEN")
url = "https://gorest.co.in/public/v2/users"
headers = {"Authorization": f"Bearer {token}"}

lista_pessoas = []
pagina = 1

while pagina <= 3:
    params = {"page": pagina, "per_page": 20}
    req = requests.get(url, headers=headers, timeout=10, params=params)

    if req.ok:
        req.raise_for_status()
        usuarios = req.json()

    pagina += 1 
    lista_pessoas.extend(usuarios) 
    print(f"Pagina atual: {pagina - 1}")
    
print(f"Todos os usuarios: {len(lista_pessoas)}")