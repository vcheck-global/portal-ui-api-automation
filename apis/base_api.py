import requests
from config.config_loader import Config


class BaseAPI:
    def __init__(self, token: str = None):
        self.base_url = Config.API_URL
        self.token = token

    def _headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def get(self, endpoint: str, params=None):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, headers=self._headers(), params=params)

    def post(self, endpoint: str, payload=None):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, json=payload, headers=self._headers())

    def put(self, endpoint: str, payload=None):
        url = f"{self.base_url}{endpoint}"
        return requests.put(url, json=payload, headers=self._headers())

    def delete(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        return requests.delete(url, headers=self._headers())
