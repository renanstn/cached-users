import os
import sys
import csv
import requests


def get_data(url):
    data = requests.get(url)
    return data.json()


def find_user_in_data(username, data):
    for user in data:
        if user['username'] == username:
            return user


def get_user(user):
    return {
        'username': user['username'],
        'email': user['email'],
        'website': user['website'],
        'hemisferio': user['hemisferio']
    }


def get_hemisphere(lat):
    return 'norte' if float(lat) > 0 else 'sul'


def save_cache(user_data):
    arquivo_ja_existe = os.path.exists('src/cache.csv')
    with open('src/cache.csv', mode='a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=user_data.keys())
        if not arquivo_ja_existe:
            writer.writeheader()
        writer.writerow(user_data)


def check_cache(user):
    if not os.path.exists('src/cache.csv'):
        return False
    with open('src/cache.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for user_cached in reader:
            if user_cached['username'] == user:
                return get_user(user_cached)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        username = sys.argv[1]
        url = 'https://jsonplaceholder.typicode.com/users'

        user_in_cache = check_cache(username)

        if user_in_cache:
            print('essa info veio do cache')
            print(user_in_cache)
        else:
            dados = get_data(url)
            user = find_user_in_data(username, dados)

            if not user:
                print("o usuário que você buscou não existe")
                sys.exit(1)

            user_hemisphere = get_hemisphere(user['address']['geo']['lat'])
            user['hemisferio'] = user_hemisphere
            user_data = get_user(user)
            save_cache(user_data)

            print('essa info foi buscada')
            print(user_data)

    else:
        print("passe um username")
