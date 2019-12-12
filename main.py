import os
import sys
import csv
import requests

def cria_cache():
    cache = open('cache.csv', 'w')
    header = 'email,website,hemisferio,username\n'
    cache.write(header)
    cache.close()


def busca_usr(username):
    busca = 0
    print('Searching in cache file.\n')
    with open('cache.csv', 'r') as arquivo:

        lista_dados = list(csv.reader(arquivo))
        for d in lista_dados[1:]:
            if d[-1].lower() == username.lower():
                print(d[0])
                print(d[1])
                print(d[2])
                busca = 1
            if busca == 1:
                break
    return busca


def busca_API(username):
    resp = requests.get('https://jsonplaceholder.typicode.com/users').json()
    print('Make request in API\n')
    for n in resp:
        if n['username'].lower() == username.lower():
            mail = n['email']
            web = n['website']
            if float(n['address']['geo']['lat']) > 0:
                hemisferio = 'Norte'
            else:
                hemisferio = 'Sul'
            usr = n['username']
            print(mail)
            print(web)
            print(hemisferio)

    f = open('cache.csv', 'a', newline='')
    adiciona = csv.writer(f)
    user = (mail, web, hemisferio, usr)
    adiciona.writerow(user)
    f.close()
    print('\nData saved in cache file.')

    return mail, web, hemisferio, usr


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        # Seu código entra aqui
        if not os.path.isfile('cache.csv'):
            cria_cache()

        s = busca_usr(username)
    
        if s == 0:
            print('username not found in cache file.\n')
            busca_API(username)
    else:
        print("passe um username")
