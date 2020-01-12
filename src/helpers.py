class Helpers:

    def get_hemisphere(self, lat):
        return 'norte' if float(lat) > 0 else 'sul'

    def get_user(self, user):
        return {
            'username': user['username'],
            'email': user['email'],
            'website': user['website'],
            'hemisphere': user['hemisphere']
        }

    def print_user(self, user):
        print('email: {}\nwebsite: {}\nhemisfério: {}'.format(
            user['email'],
            user['website'],
            user['hemisphere']
        ))
