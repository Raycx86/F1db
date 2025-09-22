import requests
import numpy as np

api_link = "https://f1api.dev/api/"


def heartbeat():
    response = requests.get(f"{api_link}heartbeat")
    print(f"Heartbeat : {response.status_code} - {response.text}")


def get_driverid(driver):
    response = requests.get(f"{api_link}drivers/search?q={driver}")

    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print(data)
        # driverid = data.get("drivers").get("driverId", "Pas de driverId")
        driverid = data.get("drivers", [{}])[0].get("driverId", "Pas de driverId")
        print(f"DriverId trouvé : {driverid}")
        return driverid
    else:
        print(f"Erreur lors de la récupération des pilotes ({response.status_code})")
        print(response.text)
        return None


def get_result(driver_result):
    print(f"{api_link}{driver_result}/drivers/{driver}")
    response = requests.get(f"{api_link}{driver_result}/drivers/{driver}")
    print(response.json())


# Utilisation
heartbeat()
driver_input = input("Quel est le pilote ? ")
driver = get_driverid(driver_input)
searched_year = input("Resultat de quelle année ? ")
driver_result = get_result(searched_year)
