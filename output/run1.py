
def test_login_to_github():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.firefox.launch()
        # Open a new browser page
        page = browser.new_page()

        try:
            # Go to GitHub login page
            page.goto("https://github.com/login")

            # Enter the username
            page.fill("#login_field", "naveennoni2429@gmail.com")

            # Enter the password
            page.fill("#password", "Github@0310")

            # Click on the "Sign in" button
            page.click("[name='commit']")

            # Navigate to the "codegendev" repository
            page.goto("https://github.com/naveennoni2429/codegendev")

            # Inside the repository, navigate to the "output" directory
            page.goto("https://github.com/naveennoni2429/codegendev/tree/main/output")

            # Inside the "output" directory, navigate to the "programs" folder
            page.goto("https://github.com/naveennoni2429/codegendev/tree/main/output/programs")

            # Inside the "programs" folder, open the "add_to_zero.py" file
            page.goto("https://github.com/naveennoni2429/codegendev/blob/main/output/programs/add_to_zero.py")

            print("Test passed")

        except Exception as ex:
            print("Test failed, element not found.")
            print(str(ex))

        finally:
            # Close the browser
            browser.close()

if __name__ == "__main__":