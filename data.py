import requests
import time


response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
data = response.json()

if response.status_code == 200:
     questions = [data['results'][i]['question'] for i in range(10)]

if response.status_code == 429:
     retry_after = response.headers.get('Retry-After', 3)  # Por defecto espera 3 segundo
     print(f"Demasiadas solicitudes, esperando {retry_after} segundos...")
     time.sleep(int(retry_after))
     







