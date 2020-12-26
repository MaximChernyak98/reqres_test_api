import configparser
from utils.http_manager import HttpManager


class Api:
    parser = configparser.ConfigParser()
    parser.read('reqres_config.ini')

    BASE_URL = parser.get('reqres', 'base_url')
    LIST_USERS = BASE_URL + 'api/users?page={0}/'

    @staticmethod
    def list_users(page: int):
        url = Api.LIST_USERS.format(page)
        result = HttpManager.get(url)
        return result
