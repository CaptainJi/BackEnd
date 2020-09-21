from time import sleep

import requests
from jenkinsapi.jenkins import Jenkins

from core.backend import jenkins
from tests.base_testcase import BaseTestCase


class TestTask(BaseTestCase):
    def test_jenkins(self):
        jenkins = Jenkins('http://www.captainnas.com:28080', username='admin',
                          password='110510b6c9f4b6ad083384608a0c3a3be9')

        jenkins['testcase'].invoke(securitytoken='110510b6c9f4b6ad083384608a0c3a3be9', build_params={
            'testcases': '.'
        })

        print(jenkins['testcase'].get_last_completed_build().get_console())

    def test_task_post(self):
        pre = jenkins['testcase'].get_last_build().get_number()
        res = requests.post('http://127.0.0.1:5000/task',
                            json={'testcases': 'sub_dir'},
                            headers={'Authorization': f'Bearer {self.token}'}
                            )
        assert res.status_code == 200
        for i in range(10):
            if not jenkins['testcase'].is_queued_or_running():
                break
            else:
                print('wait')
                sleep(1)
        last = jenkins['testcase'].get_last_build().get_number()
        assert pre + 1 == last

    def test_task_get(self):
        res = requests.get(
            'http://127.0.0.1:5000/task',
            headers={'Authorization': f'Bearer {self.token}'}
            )
        print(res.json())
        assert res.status_code == 200
