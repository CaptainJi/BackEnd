import datetime

import requests


def test_add():
    res = requests.post('http://127.0.0.1:5000/testcase',
                        json={
                            'casename': f'name{str(datetime.datetime.now())}',
                            'description': 'test description',
                            'data': 'test data'
                        })
    assert res.status_code == 200
    assert res.json()['msg'] == 'ok'
