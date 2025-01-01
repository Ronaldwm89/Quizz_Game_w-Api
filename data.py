import requests
import time

response = requests.get("https://opentdb.com/api.php?amount=11&type=boolean")
response.raise_for_status()
data = response.json()

if response.status_code == 200:
     questions = [data["results"][i]['question'] for i in range(11)]

if response.status_code == 429: # Demasiadas solicitudes
     retry_after = response.headers.get('Retry-After', 3)  # Por defecto espera 3 segundos
     print(f"Demasiadas solicitudes, espera {retry_after} segundos y vuelve a intentarlo...")
     time.sleep(int(retry_after))
     



