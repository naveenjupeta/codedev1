from playwright.sync_api import sync_playwright
import json

class AccessibilityHelper:
    @staticmethod
    def basic_accessibility_check(test_assert):
        # Start Playwright and open a browser
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            # Load the axe-core script
            with open('path/to/axe.min.js', 'r') as file:
                axe_script = file.read()

            # Navigate to the desired page
            page.goto('http://example.com')  # Replace with the actual URL

            # Inject the axe-core script into the page
            page.evaluate(axe_script)

            # Run axe-core analysis
            response_json = page.evaluate('''() => {
                return new Promise((resolve) => {
                    axe.run((err, results) => {
                        if (err) throw err;
                        resolve(results);
                    });
                });
            }''')

            # Parse the JSON response
            violations = response_json['violations']

            # Check for violations and log results
            if len(violations) == 0:
                print("PASS: basicAccessibilityCheck | No violations found.")
            else:
                # Log the results to a file or console
                with open('axe_results.json', 'w') as result_file:
                    json.dump(response_json, result_file, indent=2)
                test_assert.set_pass(False)
                print(f"FAIL: {test_assert.get_test_name()} {json.dumps(violations, indent=2)}")

            # Close the browser