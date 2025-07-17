
class WebDriverBase:
    browser = None
    context = None
    page = None

    @staticmethod
    def get_web_driver(browser_type):
        with sync_playwright() as p:
            if browser_type == "chrome":
                # Launching Chrome Browser
                WebDriverBase.browser = p.chromium.launch(headless=False)
                WebDriverBase.context = WebDriverBase.browser.new_context()
                WebDriverBase.page = WebDriverBase.context.new_page()
                WebDriverBase.page.goto('about:blank')  # Open a blank page
                WebDriverBase.page.evaluate("() => { window.localStorage.clear(); }")  # Clear local storage

            elif browser_type == "firefox":
                # Launching Firefox Browser
                WebDriverBase.browser = p.firefox.launch(headless=False)
                WebDriverBase.context = WebDriverBase.browser.new_context()
                WebDriverBase.page = WebDriverBase.context.new_page()
                WebDriverBase.page.goto('about:blank')  # Open a blank page
                WebDriverBase.page.evaluate("() => { window.localStorage.clear(); }")  # Clear local storage

            elif browser_type == "seleniumGrid":
                # Launching Browser Using Selenium Grid - Chrome Browser
                # Note: Playwright does not support Selenium Grid directly. This is a placeholder.
                raise NotImplementedError("Selenium Grid is not directly supported by Playwright.")

            else:
                raise RuntimeError(f"Browser Type {browser_type}, not Found, please add additional code for this desired WebDriver Type.")

    @staticmethod
    def close_browser():
        if WebDriverBase.page:
            WebDriverBase.page.close()
        if WebDriverBase.context:
            WebDriverBase.context.close()
        if WebDriverBase.browser: