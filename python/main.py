import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = '92d7c9b93171d6edde55801739328fcd'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}


body_create = {
    "name": "Маруся1",
    "photo_id": 32
}

body_change = {
    "pokemon_id": "73611",
    "name": "Бульба",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "73611"
}



response = requests.post(url = f'{URL}/v2/pokemons',  headers = HEADER, json = body_create)
print(response.text)


response_change =  requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_change)
print(response.text)

response = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response.text)

