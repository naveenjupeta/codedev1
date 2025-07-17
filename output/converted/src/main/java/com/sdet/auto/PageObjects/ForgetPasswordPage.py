
class ForgetPasswordPage:
    # Selectors for the email input and retrieve password button
    txt_email = "#email"
    btn_retrieve_password = ".icon-2x.icon-signin"

    def __init__(self, page):
        self.page = page

    def enter_email(self, email):
        # Fill the email input field with the provided email
        self.page.fill(self.txt_email, email)

    def click_retrieve_button(self):
        # Click the retrieve password button
        self.page.click(self.btn_retrieve_password)

# Example usage
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    forget_password_page = ForgetPasswordPage(page)
    forget_password_page.enter_email("example@example.com")
    forget_password_page.click_retrieve_button()