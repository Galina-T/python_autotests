import requests

host = "https://api.pokemonbattle.me:9104"
content_type = "application/json"
token = "221cc825969a490152a32fe1a7043782"
photo = "https://dolnikov.ru/pokemons/albums/111.png"
new_photo = "https://dolnikov.ru/pokemons/albums/017.png"
name_pokemon = "pip"
new_name_pokemon = "pip3"
pokemon_id_default = "5903"

response_create_pokemon = requests.post(f'{host}/pokemons', json={
    "name": name_pokemon,
    "photo": photo
}, headers={"Content-Type": content_type, "trainer_token": token})

response_create_pokemon_json = response_create_pokemon.json()

if response_create_pokemon_json['message'] == "Максимум 5 живых покемонов":
    pokemon_id = pokemon_id_default
else:
    pokemon_id = response_create_pokemon_json["id"]

print(response_create_pokemon_json)

response_name_change_pokemon = requests.put(f'{host}/pokemons', json={
    "pokemon_id": pokemon_id,
    "name": new_name_pokemon,
    "photo": new_photo
}, headers={"Content-Type": content_type, "trainer_token": token})

print(response_name_change_pokemon.json())

response_catch_pokemon = requests.post(f"{host}/trainers/add_pokeball", json={
    "pokemon_id": pokemon_id
}, headers={"Content-Type": content_type, "trainer_token": token})

print(response_catch_pokemon.json())
