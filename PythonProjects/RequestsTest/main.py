import requests

Url = 'https://api.pokemonbattle.ru/v2'
Token = '38493b117ce80971798fcbe7689d399f'
Header = {'Content-Type' : 'application/json', 'trainer_token':Token}
body = {
    "name": "generate",
    "photo_id": -1
}

body_name = {
    "pokemon_id": "43365",
    "name": "New Name",
    "photo_id": 2
}

'''response = requests.post(url = f'{Url}/pokemons' , headers = Header , json = body)
print(response.text)'''

'''response_add_pokeball = requests.post(url = f'{Url}/trainers/add_pokeball' , headers = Header , json = body)
print(response_add_pokeball.text)'''

'''pokemon_id = response.text['id']
print(pokemon_id)'''

'''response_name = requests.put(url = f'{Url}/pokemons' , headers = Header , json = body_name)
print(response_name.text)'''