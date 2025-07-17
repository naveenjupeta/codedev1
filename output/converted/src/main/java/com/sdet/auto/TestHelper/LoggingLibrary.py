
class LoggingLibrary:

    @staticmethod
    def compare_result(actual, expected):
        # Compare actual and expected values for equality
        if actual == expected:
            LoggingLibrary.write_line(f"PASS: Actual({actual}) | Expected({expected})")
            return True
        else:
            LoggingLibrary.write_line(f"FAIL: Actual({actual}) | Expected({expected})")
            return False

    @staticmethod
    def compare_result_contains(actual, expected):
        # Check if actual contains expected
        if expected in actual:
            LoggingLibrary.write_line(f"PASS: Actual({actual}) | ExpectedToContain({expected})")
            return True
        else:
            LoggingLibrary.write_line(f"FAIL: Actual({actual}) | ExpectedToContain({expected})")
            return False

    @staticmethod
    def write_line(message):
        # Print the message to the console
        print(message)

# Example usage with Playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://example.com')
    
    # Example assertions using the LoggingLibrary
    LoggingLibrary.compare_result(page.title(), "Example Domain")
    LoggingLibrary.compare_result_contains(page.content(), "Example Domain")
    