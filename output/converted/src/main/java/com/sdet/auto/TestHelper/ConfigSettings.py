from playwright.sync_api import sync_playwright

# Define a function to read configuration settings
def get_config_settings():
    # Initialize a dictionary to hold properties
    properties = {}
    
    # Define the properties file name
    prop_file_name = "config.properties"
    
    # Open and read the properties file
    with open(prop_file_name, 'r') as file:
        for line in file:
            # Split each line into key and value
            key, value = line.strip().split('=')
            # Store them in the properties dictionary
            properties[key] = value
    
    # Return the properties dictionary
    return properties

# Main function to execute Playwright script
def main():
    # Get configuration settings
    config = get_config_settings()
    
    # Extract web URL and browser type from config
    web_url = config.get("webUrl")
    web_browser = config.get("webBrowser")
    
    # Start Playwright
    with sync_playwright() as p:
        # Launch the specified browser
        browser = p.__getattribute__(web_browser).launch()
        # Open a new page
        page = browser.new_page()
        # Navigate to the specified web URL
        page.goto(web_url)
        
        # Print the configuration settings
        print(f"WebUrl: {web_url}")
        print(f"WebBrowser: {web_browser}")
        
        # Close the browser
        browser.close()

# Execute the main function
if __name__ == "__main__":