import configparser
from utils.http_manager import HttpManager
from utils.json_new_user import JSON_new_user


class Api:
    parser = configparser.ConfigParser()
    parser.read('users_config.ini')

    BASE_URL = parser.get('Users', 'base_url')
    CREATE_USER = BASE_URL + 'tasks/rest/createuser/'

    @staticmethod
    def create_user():
        url = Api.CREATE_USER
        json = JSON_new_user.create_minimum_json('1@mail.ru', 'ma', '[1]', '[2]')
        result = HttpManager.post(url, json)
        return result
