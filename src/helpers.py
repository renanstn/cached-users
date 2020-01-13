class Helpers:

    def get_hemisphere(self, lat):
        '''Identifica o hemisfério do usuário de acordo com a latitude'''
        return 'norte' if float(lat) > 0 else 'sul'

    def get_user(self, user):
        '''Monta um dicionário somente com os dados de interesse do user'''
        return {
            'username': user['username'],
            'email': user['email'],
            'website': user['website'],
            'hemisphere': user['hemisphere']
        }

    def print_user(self, user):
        '''Printa os dados de forma organizada'''
        print('email: {}\nwebsite: {}\nhemisfério: {}'.format(
            user['email'],
            user['website'],
            user['hemisphere']
        ))
