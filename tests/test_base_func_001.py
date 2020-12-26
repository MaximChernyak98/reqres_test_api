import pytest
from utils.users_rest_api import Api


class TestBaseFunc001:

    def test_list_users(self):
        result = Api.create_user()
        print(result._content)
        assert 200 == result.status_code
