import requests
import pandas as pd

lista_pkm = []
pkm = 1
seu_pkm  = []


class Resquest_pet:
    def __init__(self,escolha):
        self.escolha = escolha
        if escolha:
            url = f'https://pokeapi.co/api/v2/pokemon/{escolha}/'
            response = requests.get(url, timeout=3)
            pkms_data = response.json()
            
            datapk = pd.Series(pkms_data, name='Seu pokemon')
            pkm_sts = pd.DataFrame(datapk, index=['name', 'height', 'weight'])
        print(pkm_sts)



for i in range(1):
    url = f'https://pokeapi.co/api/v2/pokemon/{pkm}/'
    response = requests.get(url, timeout=3)
    pkms_data = response.json()
    if response.status_code == 200:
        
        lista_pkm.append([pkms_data['name']])
    else:
        print('Todos os pokemons morreram')
    pkm = pkm + 1


print(lista_pkm)
escolha = input('\nEscolha um pokemon\n')



        


Resquest_pet(escolha)
