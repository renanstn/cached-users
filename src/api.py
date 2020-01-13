import requests


class Api:

    def __init__(self):
        self.url = 'https://jsonplaceholder.typicode.com/users'

    def get_data(self):
        '''Busca os dados na API'''
        try:
            data = requests.get(self.url)
            self.data = data.json()
        except:
            print('houve um problema na comunicação com a API.')
            sys.exit(1)

    def find_user(self, username):
        '''Varre os dados em busca do username solicitado'''
        for user in self.data:
            if user['username'] == username:
                return user
