import requests

# 用于获取token
class BaseTestCase:

    def setup_class(self):
        username = 'captain'
        password = '1'
        res = requests.post('http://127.0.0.1:5000/login',
                            json={
                                'username': username,
                                'password': password
                            })
        print(res.text)
        assert res.status_code == 200
        self.token = res.json()['token']
        assert self.token is not None
