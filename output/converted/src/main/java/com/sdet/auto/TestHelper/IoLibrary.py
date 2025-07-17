from playwright.sync_api import sync_playwright
import time
import socket
from datetime import datetime
import os

class IoLibrary:
    _test_name = None

    @staticmethod
    def get_test_name():
        # Return the current test name
        return IoLibrary._test_name

    @staticmethod
    def set_test_name(test_name):
        # Set the test name
        IoLibrary._test_name = test_name

    @staticmethod
    def write_line(text):
        # Print a formatted line with the provided text
        print(" ")
        print(f"### {text} ###")

    @staticmethod
    def writeline_end():
        # Print the end line format
        print("############")
        print(" ")

    @staticmethod
    def get_user_name():
        # Get the hostname of the local machine
        try:
            return socket.gethostname()
        except Exception as ex:
            print("Not able to retrieve Hostname of local machine")
            return "userNameNotFound"

    @staticmethod
    def get_unique_identifier():
        # Get a unique identifier based on the current date and time
        return datetime.now().strftime("%m%d%Y%H%M%S")

    @staticmethod
    def sleep(milliseconds):
        # Sleep for the specified number of milliseconds
        time.sleep(milliseconds / 1000.0)

    @staticmethod
    def get_dir_path():
        # Get the current directory path
        return os.path.abspath(os.path.dirname('.'))

# Example usage with Playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    # Use IoLibrary methods as needed
    IoLibrary.write_line("Starting test")
    IoLibrary.set_test_name("Sample Test")
    print(IoLibrary.get_test_name())
    IoLibrary.sleep(1000)
    IoLibrary.writeline_end()