from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initializes the browser automatically
options = webdriver.ChromeOptions()
# Adds a common User-Agent to simulate a real browser and avoid basic rendering blocks
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Replace with your local URL or test page
    driver.get("https://example.com")
    time.sleep(3) # Waits for the page to load
    
    # EXAMPLE SCRIPT: Removes an annoying element (like a registration pop-up or overlay)
    # In simple paywall reverse engineering, developers identify the block ID and delete it.
    javascript_remove_block = """
    var overlay = document.querySelector('.modal-cadastro, #paywall-banner, .overlay-premium');
    if (overlay) {
        overlay.remove();
        document.body.style.overflow = 'auto'; // Restores the page scrollbar
        console.log('Obstructive element successfully removed!');
    } else {
        console.log('No blocking element found.');
    }
    """
    
    # Executes the JavaScript code inside the opened page
    driver.execute_script(javascript_remove_block)
    
    # Captures the clean text for backup or accessibility analysis purposes
    text_content = driver.find_element("tag name", "body").text
    print("\n--- Rendered Content ---")
    print(text_content[:500] + "... (truncated)")

finally:
    time.sleep(5)
    driver.quit()
