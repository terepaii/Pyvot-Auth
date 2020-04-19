"""
Loadtesting REST client
Gives graphs of the running process

In current directoy, run:

locust --host=http://127.0.0.1:5000

to point loadtesting client at the running server. Open in browser to configure
"""

import json
import uuid
from locust import HttpLocust, TaskSet, between

def register(l):
    payload =  {'Login':'test_user', 'Password':'test_user'}
    headers = {'content-type': 'application/json'}
    l.client.post("/authentication/register", data=json.dumps(payload), headers=headers)

def login(l):
    payload =  {'Login':'test_user', 'Password':'test_user'}
    headers = {'content-type': 'application/json'}
    l.client.post("/authentication/login", data=json.dumps(payload), headers=headers)

def config(l):
    pass


class UserBehavior(TaskSet):
    tasks = {config: 1, register: 2, login: 3}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)