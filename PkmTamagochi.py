import requests

lista_pkm = []
url = f'https://pokeapi.co/api/v2/pokemon/{id}/'
pkm = 1



for i in range(10):
    url = f'https://pokeapi.co/api/v2/pokemon/{pkm}/'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        
        lista_pkm.append(data['name'])
    else:
        print('Todos os pokemons morreram')
    pkm = pkm + 1


print(lista_pkm)
print(' ')
escolha = input('Escolha um pokemon\n')

