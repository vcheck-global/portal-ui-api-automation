import requests
import os

from apis.endpoints import PROJECTS_ENDPOINT


class ProjectAPI:
    def __init__(self, access_token: str):
        self.base_url = os.getenv("BASE_URL")
        self.access_token = access_token

    def get_projects(self):
        url = f"{self.base_url}{PROJECTS_ENDPOINT}"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
