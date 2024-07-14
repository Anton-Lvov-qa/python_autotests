import requests
import pytest

Url = 'https://api.pokemonbattle.ru/v2'
Token = '38493b117ce80971798fcbe7689d399f'
Header = {'Content-Type' : 'application/json', 'trainer_token':Token}
Trainer_id = '4353'

def test_trainer():
    response = requests.get(url=  f'{Url}/trainers', params= {'trainer_id': Trainer_id})
    assert response.status_code == 200

    