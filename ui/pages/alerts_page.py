# alerts_page.py
from ui.locators.alerts_locators import ALERTS_MODULE, ALERTS_TITLE
from ui.pages.base_page import BasePage


class AlertsPage:
    @staticmethod
    def navigate_to_alerts():
        BasePage.click(ALERTS_MODULE)
        BasePage.assert_visible(ALERTS_TITLE)
