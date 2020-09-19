import datetime

import requests


def test_add():
    res = requests.post('http://127.0.0.1:5000/login',
                        json={
                            'username': f'username{str(datetime.datetime.now())}',
                            'password': '12345678',
                            'email': 'test@test.com'
                        })
    assert res.status_code == 200
    assert res.json()['msg'] == 'ok'