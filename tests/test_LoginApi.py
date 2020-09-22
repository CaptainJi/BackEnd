import requests


def test_login_post():
    username = 'captain'
    password = '1'
    res = requests.post('http://127.0.0.1:5000/login',
                        json={
                            'username': username,
                            'password': password
                        })
    print(res.text)
    assert res.status_code == 200
    token = res.json()['token']
    assert token is not None

    res = requests.get(
        'http://127.0.0.1:5000/login',
        json={
            'username': username,
        },
        headers={'Authorization': f'Bearer {token}'}
    )
    print(res.json())
    assert res.status_code == 200
