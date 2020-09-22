import requests

from tests.base_testcase import BaseTestCase


def test_register_post():
    username = '测试账户3'
    password = '12345678'
    email = 'test3@163.com'
    res = requests.post('http://127.0.0.1:5000/register',
                        json={
                            'username': username,
                            'password': password,
                            'email': email
                        })
    print(res.json())
    assert res.status_code == 200
    assert res.json()['msg'] == 'ok'
