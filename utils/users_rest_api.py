import configparser
from utils.http_manager import HttpManager
from utils.json_do_register import JSON_do_register


class Api:
    parser = configparser.ConfigParser()
    parser.read('users_config.ini')

    BASE_URL = parser.get('Users', 'base_url')
    CREATE_USER = BASE_URL + 'tasks/rest/doregister'

    @staticmethod
    def create_user(user_email, user_name, user_password):
        url = Api.CREATE_USER
        json = JSON_do_register.create(user_email, user_name, user_password)
        result = HttpManager.post(url, json)
        return result
