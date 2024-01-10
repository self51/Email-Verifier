"""Service provide APIRequestManager for interaction with Hunter.io API."""

import requests


class APIRequestManager:

    def __init__(self, action: str, query_params: dict, method: str = 'get') -> None:
        self.method = method
        self.base_url = 'https://api.hunter.io/v2/'
        self.action = action
        self.query_params = ''.join(
            ['{0}={1}&'.format(key, val) for key, val in query_params.items()],
        )

    def make_request(self):
        build_url = '{0}{1}?{2}'.format(self.base_url, self.action, self.query_params)
        response = requests.request(self.method, build_url)
        return response.status_code, response.json()
