from playwright.sync_api import Page, Locator, expect


class BasePage:
    page: Page = None

    @classmethod
    def set_page(cls, page: Page):
        cls.page = page

    @classmethod
    def click(cls, selector: str):
        cls.page.click(selector)

    @classmethod
    def assert_visible(cls, selector: str):
        expect(cls.page.locator(selector)).to_be_visible(timeout=5000)

    def find(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def fill(self, selector: str, value: str, timeout: int = 5000):
        self.find(selector).wait_for(state="visible", timeout=timeout)
        self.find(selector).fill(value)

    def select_dropdown_by_value(self, selector: str, value: str):
        self.find(selector).select_option(value=value)

    def select_dropdown_by_text(self, selector: str, text: str):
        self.find(selector).select_option(label=text)

    def check_checkbox(self, selector: str):
        checkbox = self.find(selector)
        if not checkbox.is_checked():
            checkbox.check()

    def uncheck_checkbox(self, selector: str):
        checkbox = self.find(selector)
        if checkbox.is_checked():
            checkbox.uncheck()

    def upload_file(self, selector: str, file_path: str):
        self.find(selector).set_input_files(file_path)

    def wait_for_visible(self, selector: str, timeout: int = 5000):
        self.find(selector).wait_for(state="visible", timeout=timeout)

    def assert_hidden(self, selector: str):
        expect(self.find(selector)).not_to_be_visible()

    def assert_text_contains(self, selector: str, text: str):
        expect(self.find(selector)).to_contain_text(text)
