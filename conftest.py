# conftest.py
import os
import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

from utils import logger
from utils.logger import setup_logger
from apis.auth_handler import AuthHandler




# === Shared Fixtures ===
@pytest.fixture(scope="session", autouse=True)
def initialize_logger():
    setup_logger()

# === Playwright Launch Fixture ===
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

# === UI Fixtures ===
@pytest.fixture(scope="session")
def browser(playwright_instance) -> Browser:
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=100)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext, request) -> Page:
    page = context.new_page()
    page.set_viewport_size({"width": 1500, "height": 800})
    yield page

    # Take screenshot on failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        path = f"screenshots/{request.node.name}.png"
        page.screenshot(path=path)
        logger.info(f"\n[Playwright] Screenshot saved at: {path}")

    page.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# === API Fixtures ===
@pytest.fixture(scope="session")
def auth_handler():
    return AuthHandler()


