import os
from PIL import Image, ImageDraw, ImageFont
import io

class PlaywrightExtensions:
    def __init__(self, page):
        self.page = page

    def get_element_by_selector(self, css_selector, wait_seconds=10):
        # Wait for the element to be visible and return it
        return self.page.wait_for_selector(css_selector, timeout=wait_seconds * 1000)

    def playwright_exception_handler(self, ex):
        # Handle exceptions by logging and taking a screenshot
        exception_name = str(ex)
        print(f"Playwright Exception Handler Caught Exception: [{exception_name}]")
        self.screenshot()
        print("Exception handling complete.")

    def screenshot(self):
        # Take a screenshot and save it with a unique name
        test_name = f"test_{self.page.url.split('//')[-1].replace('/', '_')}.png"
        screenshot_dir = "target/outputs/screenshots/"
        
        if not os.path.exists(screenshot_dir):
            print("No Folder Found")
            os.makedirs(screenshot_dir)
            print(f"Folder created: [{screenshot_dir}]")

        # Capture screenshot
        screenshot_path = os.path.join(screenshot_dir, test_name)
        self.page.screenshot(path=screenshot_path)

        # Add URL text to the screenshot
        with Image.open(screenshot_path) as im:
            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype("arial.ttf", 20)
            text_to_write = self.page.url
            text_width, text_height = draw.textsize(text_to_write, font=font)
            draw.rectangle([0, 0, text_width, text_height], fill="white")
            draw.text((0, 0), text_to_write, fill="black", font=font)
            im.save(screenshot_path)

        print(f"Browser Screenshot Save Location: {screenshot_path}")

# Usage example
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://example.com')
    extensions = PlaywrightExtensions(page)
    try:
        element = extensions.get_element_by_selector('h1')
        print(element.inner_text())
    except Exception as e:
        extensions.playwright_exception_handler(e)