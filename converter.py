import requests
import json

# Obtener la moneda objetivo como entrada del usuario
currency = input()

# Realizar la solicitud GET a la URL
response = requests.get(f'https://www.floatrates.com/daily/{currency.lower()}.json')


# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a un diccionario Python
    data = response.json()

    # Especificar las monedas que deseas imprimir
    currencies_to_print = ['usd', 'eur']

    # Imprimir solo las monedas especificadas en el formato solicitado
    for currency in currencies_to_print:
        if currency in data:
            currency_data = data[currency]
            # Imprimir en el formato solicitado
            print(
                f"{{'code': '{currency_data['code']}', 'alphaCode': '{currency_data['alphaCode']}', 'numericCode': {currency_data['numericCode']}, 'name': '{currency_data['name']}', 'rate': {currency_data['rate']}, 'date': '{currency_data['date']}', 'inverseRate': {currency_data['inverseRate']}}}")
else:
    print(f"Error al obtener los datos. Código de estado: {response.status_code}")
