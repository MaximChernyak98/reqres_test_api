import pytest
from utils.reqres_api import Api


class TestBaseFunc001:

    def test_list_users(self):
        result = Api.list_users(2)
        assert 200 == result.status_code
