import pytest
from selene import browser

@pytest.fixture(scope="function",autouse=True)
def browser_options():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url='https://demoqa.com'

    yield

    browser.quit()