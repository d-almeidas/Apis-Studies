import requests

url = "https://gorest.co.in/public/v2/users"
todos=[]
pagina=1

while True:
    params =  params = {"status": "active", "page": pagina, "per_page": 50}
    req = requests.get(url, params=params, timeout=10)
    req.raise_for_status()

    usuarios=req.json()
    if not usuarios:
        break 

    todos.extend(usuarios)
    pagina+=1
    print(f"Página {pagina - 1} ok, total até agora: {len(todos)}")

print(f"Total de usuários ativos: {len(todos)}")
print(req.headers)