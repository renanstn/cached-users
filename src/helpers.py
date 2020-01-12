def get_hemisphere(lat):
    return 'norte' if float(lat) > 0 else 'sul'


def get_user(user):
    return {
        'username': user['username'],
        'email': user['email'],
        'website': user['website'],
        'hemisphere': user['hemisphere']
    }


def print_user(user):
    print('email: {}\nwebsite: {}\nhemisfério: {}'.format(
        user['email'],
        user['website'],
        user['hemisphere']
    ))
