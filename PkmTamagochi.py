import requests

lista_pkm = []
url = f'https://pokeapi.co/api/v2/pokemon/{id}/'
for i in range(1):
    pkm = 1
    url = f'https://pokeapi.co/api/v2/pokemon/{pkm}/'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        print(f'Nome do Pokemon: {data["name"]}')
    else:
        print('Todos os pokemons morreram')