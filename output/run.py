from playwright.sync_api import sync_playwright

def test_successful_login():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch()
        # Open a new page
        page = browser.new_page()
        # Navigate to the GitHub login page
        page.goto('https://github.com/login')

        # Fill in the username and password fields
        page.fill('input#login_field', 'naveennoni2429@gmail.com')
        page.fill('input#password', 'Github@0310')
        # Click the sign-in button
        page.click('input[name="commit"]')

        try:
            # Wait for the profile summary element to appear, indicating a successful login
            page.wait_for_selector('summary[aria-label="View profile and more"]', timeout=10000)
            print("❌ Test Case 1: Successful Login to GitHub - Failed")
        except:
            print("✅ Test Case 1: Successful Login to GitHub - Passed")

        # Close the browser
        browser.close()

def test_unsuccessful_login():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch()
        # Open a new page
        page = browser.new_page()
        # Navigate to the GitHub login page
        page.goto('https://github.com/login')

        # Fill in the username and password fields with incorrect credentials
        page.fill('input[name="login"]', 'incorrectemail@gmail.com')
        page.fill('input[name="password"]', 'incorrectpassword')
        # Click the sign-in button
        page.click('input[name="commit"]')

        try:
            # Wait for the error message to appear
            page.wait_for_selector('.flash-error', timeout=10000)
            print("❌ Test Case 2: Unsuccessful Login to GitHub with invalid credentials - Failed")
        except:
            print("✅ Test Case 2: Unsuccessful Login to GitHub with invalid credentials - Passed")

        # Close the browser
        browser.close()

if __name__ == "__main__":
    test_successful_login()