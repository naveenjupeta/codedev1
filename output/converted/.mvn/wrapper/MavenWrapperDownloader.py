from playwright.sync_api import sync_playwright

# Function to download a file from a URL
def download_file_from_url(url, destination):
    import requests
    response = requests.get(url)
    with open(destination, 'wb') as f:
        f.write(response.content)

# Main function to execute the Playwright script
def main():
    with sync_playwright() as p:
        # Start the browser
        browser = p.chromium.launch()
        # Open a new page
        page = browser.new_page()
        
        # Default URL to download the maven-wrapper.jar
        default_download_url = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.4.0/maven-wrapper-0.4.0.jar"
        
        # Path to the maven-wrapper.properties file
        maven_wrapper_properties_path = ".mvn/wrapper/maven-wrapper.properties"
        
        # Path where the maven-wrapper.jar will be saved
        maven_wrapper_jar_path = ".mvn/wrapper/maven-wrapper.jar"
        
        # Name of the property to override the default download URL
        property_name_wrapper_url = "wrapperUrl"
        
        # Base directory
        base_directory = "."
        
        # Check if maven-wrapper.properties exists and read the custom URL if available
        url = default_download_url
        try:
            with open(f"{base_directory}/{maven_wrapper_properties_path}", 'r') as prop_file:
                for line in prop_file:
                    if line.startswith(property_name_wrapper_url):
                        url = line.split('=')[1].strip()
                        break
        except FileNotFoundError:
            pass
        
        # Download the file
        output_file = f"{base_directory}/{maven_wrapper_jar_path}"
        download_file_from_url(url, output_file)
        
        # Close the browser
        browser.close()

# Execute the main function
if __name__ == "__main__":