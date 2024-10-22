import requests
import pytest

URL ='https://api.pokemonbattle.ru'

def tests_status_code ():
    response= requests.get(url= f'{URL}/v2/trainers')
    assert response.status_code == 200

trainer_id = '7456'
def tests_trainer_id ():
    response_trainer_id=requests.get(url= f'{URL}/v2/trainers',params= {'trainer_id':trainer_id})
    assert response_trainer_id.json()['data'][0]['id'] == trainer_id
