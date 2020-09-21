import requests

from tests.base_testcase import BaseTestCase


class TestLogin(BaseTestCase):
    def test_login_post(self):

        res = requests.get(
            'http://127.0.0.1:5000/testcase',
            headers={'Authorization': f'Bearer {self.token}'}
        )
        print(res.json())
        assert res.status_code == 200
