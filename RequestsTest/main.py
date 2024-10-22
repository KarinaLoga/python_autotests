import requests

URL ='https://api.pokemonbattle.ru'
trainer_token='TRAINER_TOKEN'
HEADER = {'Content-Type':'application/json', 'trainer_token':trainer_token}
body_create_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 1
}

response_create_pokemon = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create_pokemon.text)

body_change_name = {
    "pokemon_id":response_create_pokemon.json()['id'] ,
    "name": "Кузя",
    "photo_id": 2
}
response_change_name = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

body_add_pokeball = {'pokemon_id' : response_create_pokemon.json()['id']}
response_add_pokeball = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)