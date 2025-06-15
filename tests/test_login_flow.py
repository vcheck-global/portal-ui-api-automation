import logging

from apis.auth_handler import AuthHandler
from apis.project_api import ProjectAPI  # Adjust path as needed
import os
from dotenv import load_dotenv
from ui.pages.alerts_page import AlertsPage
from ui.pages.base_page import BasePage
from utils.ui_login import UILoginHandler

load_dotenv()
logger = logging.getLogger(__name__)


def test_full_login_flow():
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    auth = AuthHandler(email=email, password=password)
    account_id = auth.get_account_id_by_name("Test Account revamp")
    auth.login_with_account_id(account_id)

    project_api = ProjectAPI(access_token=auth.access_token)
    projects = project_api.get_projects()

    assert isinstance(projects, list) or "results" in projects
    logger.info(projects)


def test_ui_login(page):
    BasePage.set_page(page)
    ui_handler = UILoginHandler(page)
    ui_handler.login_via_ui()
    logger.info("Logged In successfully via UI")
    logger.debug("Logged In successfully via UI")
    AlertsPage.navigate_to_alerts()
