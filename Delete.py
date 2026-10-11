import requests
import os 
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GOREST_TOKEN")

headers = {"Authorization": f"Bearer {token}"}

req = requests.delete('https://gorest.co.in/public/v2/users/8660629', headers=headers)
print(req.status_code)