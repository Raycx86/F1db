import requests
import os

api_link = "https://f1api.dev/api/"
def heartbeat():
    response = requests.get(f'{api_link}heartbeat')
    print(f"Heartbeat : {response.status_code} - {response.text}")

def get_driver(driver):
    response = requests.get(f'{api_link}drivers/search?q={driver}')
    if response.status_code == 200:
        print("Pilotes :", response.json())
    else:
        print(f"Erreur lors de la récupération des pilotes ({response.status_code})")
        print(response.text)


# Utilisation
heartbeat()
driver_input = input("Quel est le pilot ? ")
get_driver(driver_input)
