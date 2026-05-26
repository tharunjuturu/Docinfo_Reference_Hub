import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def capture_screenshot():
    print("Starting screenshot capture...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1600,1200")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"Standard ChromeDriver failed: {e}. Trying generic driver bootstrap...")
        try:
            driver = webdriver.Firefox()
        except Exception as fe:
            print(f"Firefox also failed: {fe}. Capturing aborted.")
            return False

    try:
        # Load local HTML file
        local_path = os.path.abspath("index.html")
        print(f"Loading local page: file:///{local_path}")
        driver.get(f"file:///{local_path}")
        
        # Wait 3 seconds for Tailwind CDN and fonts to fully load & render
        time.sleep(3)
        
        # Save screenshot
        target_dir = r"C:\Users\tjuturu\.gemini\antigravity\brain\9a9b6771-ca41-45db-b57d-033fbfe2eb79"
        os.makedirs(target_dir, exist_ok=True)
        screenshot_path = os.path.join(target_dir, "hub_preview.png")
        
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved successfully at: {screenshot_path}")
        driver.quit()
        return True
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        try:
            driver.quit()
        except:
            pass
        return False

if __name__ == "__main__":
    capture_screenshot()
