import sys
import csv_cache
import api


def get_user(user):
    return {
        'username': user['username'],
        'email': user['email'],
        'website': user['website'],
        'hemisferio': user['hemisferio']
    }


def get_hemisphere(lat):
    return 'norte' if float(lat) > 0 else 'sul'


def print_user(user):
    print('email: {}\nwebsite: {}\nhemisfério: {}'.format(
        user['email'],
        user['website'],
        user['hemisferio']
    ))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        cache = csv_cache.CsvCache()
        api = api.Api()

        user_in_cache = cache.check_cache(username)

        if user_in_cache:
            user = get_user(user_in_cache)
            print_user(user)

        else:
            dados = api.get_data()
            user = api.find_user(username)

            if not user:
                print("o usuário que você buscou não existe")
                sys.exit(1)

            user_hemisphere = get_hemisphere(user['address']['geo']['lat'])
            user['hemisferio'] = user_hemisphere
            user_data = get_user(user)
            cache.save_cache(user_data)

            print_user(user_data)

    else:
        print("passe um username")
