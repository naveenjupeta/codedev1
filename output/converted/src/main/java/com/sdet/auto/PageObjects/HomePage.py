
class HomePage:
    # Selectors for elements on the page
    txtHeader = ".heading"
    linkForgetPassword = "[href='/forgot_password']"
    linkFormAuthentication = "[href='/login']"

    def __init__(self, page):
        self.page = page

    def click_forget_password(self):
        # Click on the "Forget Password" link
        self.page.click(self.linkForgetPassword)

    def click_form_authentication(self):
        # Click on the "Form Authentication" link
        self.page.click(self.linkFormAuthentication)

    def verify_on_home_page(self, test_assert):
        # Get the text of the header and verify it
        header_text = self.page.inner_text(self.txtHeader)
        test_assert.set_pass(header_text == "Welcome to the-internet")

# Usage example:
# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     home_page = HomePage(page)
#     home_page.click_forget_password()
#     home_page.click_form_authentication()
#     home_page.verify_on_home_page(test_assert)