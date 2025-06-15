# utils/ui_login.py
import os
from dotenv import load_dotenv
from ui.locators.login_locators import (
    LOGIN_EMAIL_SELECTOR,
    LOGIN_PASSWORD_SELECTOR,
    LOGIN_SUBMIT_SELECTOR,
    DASHBOARD_SELECTOR
)

load_dotenv()


class UILoginHandler:
    def __init__(self, page):
        self.page = page
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.login_url = os.getenv("LOGIN_URL")

    def login_via_ui(self):
        self.page.goto(self.login_url)
        self.page.fill(LOGIN_EMAIL_SELECTOR, self.email)
        self.page.click(LOGIN_SUBMIT_SELECTOR)
        self.page.fill(LOGIN_PASSWORD_SELECTOR, self.password)
        self.page.click(LOGIN_SUBMIT_SELECTOR)
        self.page.wait_for_selector(DASHBOARD_SELECTOR)
