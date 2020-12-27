try:
    import json
    import pytest
    import sys
    import os
    from datetime import datetime
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
finally:
    from utils.users_rest_api import Api


class TestBaseFunc001:

    def generate_user_data(self):
        # create parameters for unic user
        now = datetime.now()
        user_email = 'm' + now.strftime("%Y%m%d_%H%M%S%f") + '@mail.ru'
        user_name = 'm' + now.strftime("%Y%m%d_%H%M%S%f")
        user_password = '1234'
        return user_email, user_name, user_password

    def test_do_register(self):
        user_email, user_name, user_password = self.generate_user_data()
        result = Api.create_user(user_email, user_name, user_password)
        result_json = json.loads(result.content)

        assert 200 == result.status_code and user_name == result_json['name']

    def test_email_do_register(self):
        user_email, _, _ = self.generate_user_data()
        result = Api.create_user(user_email, '', '')
        result_json = json.loads(result.content)
        assert result_json['type'] == 'error'


if __name__ == "__main__":
    a = TestBaseFunc001()
    a.test_email_do_register()
