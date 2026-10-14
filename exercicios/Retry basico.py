import os 
import time
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GOREST_TOKEN")
header = {"Authorization": f"Bearer {token}"}

def get_with_retry(url, header=header, tentativas=3, espera=2, **kwargs):
    for tentativa in range(1, tentativas + 1):
        try:
            req = requests.get(url, timeout=10, **kwargs)
            req.raise_for_status()
            return req
        
        except requests.exceptions.Timeout:
            print("A api demorou dms")
        except requests.exceptions.ConnectionError:
            print("Error de conexäo")
            
        if tentativa < tentativas:
            print('Testando...')
            time.sleep(espera)
            tentativa += 1
            continue

    raise Exception("A API não respondeu depois de várias tentativas.")

req = get_with_retry("https://goraest.co.in/public/v2/users")
print(req.status_code)
print(req.json())