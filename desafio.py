import requests
import hashlib

import json


req = None

def requisicao():

    try:

        req = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' )

        desafio = req.json()

        return desafio

    except:

        print('Erro na conexão')

        return None


desafio = requisicao()

n_casas = 1

mensagem= desafio['cifrado']


def decifrado(mensagem, n_casas):
    '''função utilizada estritamente
    para obtenção da mensagem decifrada.'''

    decifrar = ''

    for count in mensagem:

         if 'a' <= count <= 'z':

                decifrar += chr(ord(count) - n_casas)
         else:
            decifrar += count

    return decifrar


desafio['decifrado'] += decifrado(mensagem, n_casas)



def resumo(resumo_cript):

    h = hashlib.sha1()

    h.update(resumo_cript.encode())

    return h.hexdigest()

p = resumo(desafio['decifrado'])


desafio['resumo_criptografico'] += p


with open('answer.json', 'wt', encoding='utf-8') as file:

    file.write(json.dumps(desafio, indent=4))

site = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='

filename = 'answer.json'

up = {'answer':(filename, open(filename, 'rb'), "multipart/form-data")}

request = requests.post(site, files=up)

print(request.status_code)



