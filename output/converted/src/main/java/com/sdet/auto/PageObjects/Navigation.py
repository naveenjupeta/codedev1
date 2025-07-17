from config_settings import ConfigSettings  # Assuming ConfigSettings is defined in a separate module

class Navigation:
    @staticmethod
    def nav_to_web_page_under_test():
        with sync_playwright() as p:
            # Launch the browser
            browser = p.chromium.launch()
            # Open a new browser page
            page = browser.new_page()
            # Navigate to the URL specified in ConfigSettings
            page.goto(ConfigSettings.get_web_url())
            # Close the browser after navigation