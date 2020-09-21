import datetime

import requests


class TestTestCaseApi():
    def test_add_testcase(self):
        res = requests.post('http://127.0.0.1:5000/testcase',
                            json={
                                # 'casename': f'name{str(datetime.datetime.now())}',
                                'casename': '测试',
                                'description': '测试数据',
                                'data': 'test data'
                            })
        print(res.json())
        assert res.status_code == 200
        assert res.json()['msg'] == 'ok'

    def test_testcase_get(self):
        res = requests.get(
            'http://127.0.0.1:5000/testcase'
        )
        print(res.json())
        # assert res.status_code == 200

    def test_testcase_put(self):
        casename = '测试'
        description = '测试数据'
        update_casename = '更新后测试'
        update_description = '更新后描述'
        update_data = '更新后数据'
        res = requests.put('http://127.0.0.1:5000/testcase',
                           json={
                               'casename': casename,
                               'description': description,
                               'update_casename': update_casename,
                               'update_description': update_description,
                               'update_data': update_data
                           })

        print(res.json())
        assert res.status_code == 200
        assert res.json()['msg'] == 'update success'

    def test_testcase_del(self):
        casename = '更新后测试'
        description = '更新后描述'
        res = requests.delete('http://127.0.0.1:5000/testcase',
                              json={
                                  'casename': casename,
                                  'description': description,
                              })
        print(res.json())
        assert res.status_code == 200
        assert res.json()['msg'] == 'delete success'
