
class GuiHelper:
    browser = None
    context = None
    page = None

    @staticmethod
    def open_web_browser():
        # Start Playwright and launch the browser
        playwright = sync_playwright().start()
        GuiHelper.browser = playwright.chromium.launch(headless=False)
        GuiHelper.context = GuiHelper.browser.new_context()
        GuiHelper.page = GuiHelper.context.new_page()

    @staticmethod
    def open_web_browser_with_context(context):
        # Use the provided context to open a new page
        GuiHelper.page = context.new_page()

    @staticmethod
    def close_web_browser():
        # Close the page, context, and browser
        if GuiHelper.page:
            GuiHelper.page.close()
        if GuiHelper.context:
            GuiHelper.context.close()
        if GuiHelper.browser: