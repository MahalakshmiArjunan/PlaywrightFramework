import pytest

@pytest.fixture(scope='function')
def browser_context(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context()
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope='function')
def page(browser_context, base_url):
    page = browser_context.new_page()
    page.goto(base_url)
    yield page
    page.close()

