
class SecureAreaPage:
    # Selectors for the message label and logout button
    lbl_message = "#flash"
    btn_logout = ".icon-2x.icon-signout"

    def __init__(self, page):
        self.page = page

    def verify_message(self, expected_msg):
        # Get the text from the message label and check if it contains the expected message
        actual_msg = self.page.inner_text(self.lbl_message)
        assert expected_msg in actual_msg, f"Expected message '{expected_msg}' not found in '{actual_msg}'"

    def click_logout_button(self):
        # Click the logout button
        self.page.click(self.btn_logout)

# Example usage with Playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com/secure-area")  # Replace with the actual URL

    secure_area_page = SecureAreaPage(page)
    secure_area_page.verify_message("Expected Message")  # Replace with the actual expected message
    secure_area_page.click_logout_button()
