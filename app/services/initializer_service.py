import json

class InitializerService:
    filename = 'app/data/users.json'

    @classmethod
    def get_channels_from_json(cls):
        with open(cls.filename, 'r') as file:
            data = json.load(file)
            return data['channels']


    @classmethod
    def get_subscriptions_from_json(cls):
        with open(cls.filename, 'r') as file:
            data = json.load(file)
            return data['subscriptions']

    @classmethod
    def get_users_from_json(cls):
        with open(cls.filename, 'r') as file:
            data = json.load(file)
            return data['users']