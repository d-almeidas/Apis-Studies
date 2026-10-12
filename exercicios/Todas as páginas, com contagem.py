import os
import requests
from dotenv import load_dotenv
import rich

load_dotenv()
token = os.getenv("GOREST_TOKEN")
url = "https://gorest.co.in/public/v2/users"
headers = {"Authorization": f"Bearer {token}"}

contagem = {"male": 0, "female": 0}
total = 0
pagina = 1
LIMITE_PAGINAS = 20

while pagina <= LIMITE_PAGINAS:
    params = {"status": "inactive", "page": pagina, "per_page": 100}
    req = requests.get(url, headers=headers, timeout=10, params=params)
    req.status_code

    usuarios = req.json()
    if not usuarios:
        break
    
    for pessoa in usuarios:
        contagem[pessoa["gender"]] += 1

    total += len(usuarios)
    pagina += 1
    print(f"Pagina atual: {pagina - 1} ok, total ate agora: {total}")

print(f"total de pessoas: {total}")
print(f"total de homens: {contagem['male']}")
print(f"total de mulheres: {contagem['female']}")
print('[bold red]Erro![/bold red]')