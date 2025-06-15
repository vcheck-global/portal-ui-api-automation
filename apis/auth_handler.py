import os
import requests
from dotenv import load_dotenv

from apis.endpoints import LOGIN_ENDPOINT, USER_ME_ENDPOINT, LOGIN_WITH_ACCOUNT_ENDPOINT, PROJECTS_ENDPOINT

# Load environment variables from .env file
load_dotenv()


class AuthHandler:
    BASE_URL = os.getenv("BASE_URL")

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.access_token = None
        self.refresh_token = None
        self.account_id = None
        self.login()

    def login(self):
        url = f"{self.BASE_URL}{LOGIN_ENDPOINT}"
        response = requests.post(url, json={"email": self.email, "password": self.password})
        response.raise_for_status()
        tokens = response.json()
        self.access_token = tokens["access"]
        self.refresh_token = tokens["refresh"]

    def get_account_id_by_name(self, account_name: str) -> int:
        url = f"{self.BASE_URL}{USER_ME_ENDPOINT}"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        accounts = response.json().get("accounts", [])
        for account in accounts:
            if account["name"] == account_name:
                self.account_id = account["id"]
                return self.account_id
        raise ValueError(f"Account '{account_name}' not found.")

    def login_with_account_id(self, account_id: int):
        url = f"{self.BASE_URL}{LOGIN_WITH_ACCOUNT_ENDPOINT}"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.post(url, json={"account_id": account_id}, headers=headers)
        response.raise_for_status()
        tokens = response.json()
        self.access_token = tokens["access"]
        self.refresh_token = tokens["refresh"]
