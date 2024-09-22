import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = '92d7c9b93171d6edde55801739328fcd'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
trainer_id = '4716'

def test_status_code():
    responce = requests.get(url = f'{URL}/v2/pokemons', params = {'trainer_id': trainer_id})
    assert responce.status_code == 200

    
    @pytest.mark.parametrize('key, value', [('trainer_id', trainer_id)])
    def test_parametrize(key, value):
        responce_parametrize = requests.get(url = f'{URL}/v2/pokemons', params = {'trainer_id': trainer_id})
        assert responce_parametrize.json()["data"][0][key] == value