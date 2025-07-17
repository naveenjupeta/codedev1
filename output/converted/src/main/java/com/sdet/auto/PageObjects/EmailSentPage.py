
class EmailSentPage:
    # Selector for the message element
    txt_message = "#content"

    def __init__(self, page):
        # Initialize with a Playwright page instance
        self.page = page

    def verify_email_sent(self, test_assert, expected_msg):
        # Get the text content of the message element
        actual_msg = self.page.text_content(self.txt_message)
        # Compare the actual message with the expected message
        test_assert.set_pass(actual_msg == expected_msg)

# Usage example
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    email_sent_page = EmailSentPage(page)
    # Assuming test_assert is an instance of a TestAssert-like class
    email_sent_page.verify_email_sent(test_assert, "Expected message")