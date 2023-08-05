import requests
import pytest

host = "https://api.pokemonbattle.me:9104"
trainer_id = 1224


def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200


@pytest.mark.parametrize("key, value", [("trainer_name", "Galka")])
def test_response_has_trainer_name(key,  value):
    response = requests.get(
        f'{host}/trainers', params={'trainer_id': trainer_id})
    response_text = response.json()
    assert response_text[key] == value
