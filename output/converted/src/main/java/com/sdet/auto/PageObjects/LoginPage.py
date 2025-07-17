
class LoginPage:
    # Selectors for the elements on the login page
    txt_username = "#username"
    txt_password = "#password"
    btn_login = ".fa.fa-2x.fa-sign-in"
    lbl_message = "#flash"

    def __init__(self, page):
        self.page = page

    def enter_credentials(self, user_id, password):
        # Fill in the username and password fields and click the login button
        self.page.fill(self.txt_username, user_id)
        self.page.fill(self.txt_password, password)
        self.page.click(self.btn_login)

    def verify_message(self, test_assert, expected_msg):
        # Verify that the message contains the expected text
        actual_msg = self.page.inner_text(self.lbl_message)
        test_assert.set_pass(expected_msg in actual_msg)

# Example usage
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    login_page = LoginPage(page)
    page.goto("http://example.com/login")  # Navigate to the login page
    login_page.enter_credentials("user", "pass")
    login_page.verify_message(test_assert, "expected message")