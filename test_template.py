import os
import requests


class APITest:
    API_ADDRESS = '0.0.0.0'
    API_PORT = 8000
    OUTPUT = '''
    ============================
        {test_type} test
    ============================

    request done at {endpoint}
    | username={username}
    | password={password}

    expected result = 200
    actual result = {status_code}

    ==>  {test_status}
    '''

    def __init__(self, endpoint, test_type):
        self.endpoint = endpoint
        self.test_type = test_type
        self.params = {
            'username': '',
            'password': ''
        }

    def test_endpoint(self, username, password, *args, **kwargs):
        self.params['username'] = username
        self.params['password'] = password
        self.params['sentence'] = kwargs.get('sentence')

        r = requests.get(
            url='http://{address}:{port}/{endpoint}'.format(address=self.API_ADDRESS,
                                                            port=self.API_PORT,
                                                            endpoint=self.endpoint),
            params=self.params
        )

        test_status = self.test_condition(r, *args, **kwargs)

        test_results = self.OUTPUT.format(endpoint=self.endpoint,
                                          test_type=self.test_type,
                                          username=username,
                                          password=password,
                                          status_code=r.status_code,
                                          test_status=test_status)

        if os.environ.get('LOG') == '1':
            with open('api_test.log', 'a') as file:
                file.write(test_results)

    def test_condition(self, request, *args, **kwargs):
        if request.status_code == 200:
            test_status = 'SUCCESS'
        else:
            test_status = 'FAILURE'

        print(test_status, request.status_code, request.text)
        return test_status
