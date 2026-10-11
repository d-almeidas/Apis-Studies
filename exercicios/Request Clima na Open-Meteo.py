
import requests

url="https://api.open-meteo.com/v1/forecast"

params = {"latitude": -12.15, "longitude": -44.99, "current_weather": True}
req = requests.get(url,timeout=10, params=params)

if req.ok:
    print(req.status_code)
    infos=req.json()
    print(infos)
else:
    print(f"error: {req.status_code, req.text}")