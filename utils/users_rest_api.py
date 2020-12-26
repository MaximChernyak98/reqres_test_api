import configparser
from utils.http_manager import HttpManager
from utils.json_do_register import JSON_do_register


class Api:
    parser = configparser.ConfigParser()
    parser.read('users_config.ini')

    BASE_URL = parser.get('Users', 'base_url')
    CREATE_USER = BASE_URL + 'tasks/rest/doregister'

    @staticmethod
    def create_user():
        url = Api.CREATE_USER
        json = JSON_do_register.create('1@mail.ru', 'ma', '1')
        result = HttpManager.post(url, json)
        return result
