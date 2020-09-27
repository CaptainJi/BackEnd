from time import sleep

import requests
from jenkinsapi.jenkins import Jenkins

from core.backend import jenkins
from tests.base_testcase import BaseTestCase


class TestTask(BaseTestCase):
    # 测试jenkins调度功能是否正常运行
    def test_jenkins(self):
        jenkins = Jenkins('http://www.captainnas.com:28080', username='admin',
                          password='110510b6c9f4b6ad083384608a0c3a3be9')

        jenkins['testcase'].invoke(securitytoken='110510b6c9f4b6ad083384608a0c3a3be9', build_params={
            'testcases': '.'
        })

        print(jenkins['testcase'].get_last_completed_build().get_console())
        print(jenkins.get_jobs_list())
        print(jenkins.keys())

    # 发起jenkins构建请求
    def test_task_post(self):
        # 获取上一次成功构建号码
        pre = jenkins['testcase'].get_last_build().get_number()
        res = requests.get \
            ('http://127.0.0.1:5000/task',
             json={'testcases': 'sub_dir'},
             headers={'Authorization': f'Bearer {self.token}'}
             )
        assert res.status_code == 200
        # 判断当前是否有项目正在构建
        for i in range(10):
            if not jenkins['testcase'].is_queued_or_running():
                break
            else:
                print('wait')
                sleep(1)
        # 获取最后一次成功构建号码
        last = jenkins['testcase'].get_last_build().get_number()
        assert pre + 1 == last

    # 获取所有构建任务信息
    def test_task_get(self):
        res = requests.get(
            'http://127.0.0.1:5000/task',
            headers={'Authorization': f'Bearer {self.token}'}
        )
        print(res.json())
        assert res.status_code == 200
