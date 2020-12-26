import pytest
import json

from utils.users_rest_api import Api


class TestBaseFunc001:

    def test_do_register(self):
        result = Api.create_user()
        result_json = json.loads(result.content)
        print(result_json)

        assert 200 == result.status_code
