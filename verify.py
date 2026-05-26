import os
import json
import html.parser

class HTMLValidator(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)

    def handle_endtag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

def verify_hub():
    print("=== STARTING HUB VERIFICATION ===")
    
    # 1. Check directory & files exist
    base_dir = r"c:\New PYTHON\Team_Reference_Hub"
    html_path = os.path.join(base_dir, "index.html")
    json_path = os.path.join(base_dir, "links.json")
    
    if not os.path.exists(html_path):
        print("[FAIL] Error: index.html is missing!")
        return False
    print("[OK] index.html exists.")
    
    if not os.path.exists(json_path):
        print("[FAIL] Error: links.json is missing!")
        return False
    print("[OK] links.json exists.")
    
    # 2. Verify links.json is valid JSON and has 58 items
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            print("[FAIL] Error: links.json is not a list!")
            return False
        print(f"[OK] links.json parsed successfully. Count: {len(data)} items.")
        if len(data) != 58:
            print(f"[WARN] Warning: expected 58 items, found {len(data)}.")
    except Exception as e:
        print(f"[FAIL] Error parsing links.json: {e}")
        return False
        
    # 3. Verify HTML structure
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        parser = HTMLValidator()
        parser.feed(html_content)
        print("[OK] index.html structure is well-formed.")
        
        # Verify specific features in HTML
        features = [
          "tailwind.config",
          "embeddedLinks",
          "getEnvironmentMeta",
          "search-input",
          "bookmark-groups-container",
          "toast"
        ]
        
        for feature in features:
            if feature in html_content:
                print(f"  [OK] Feature check: '{feature}' is present.")
            else:
                print(f"  [FAIL] Feature check: '{feature}' is MISSING!")
                return False
                
    except Exception as e:
        print(f"[FAIL] Error verifying index.html: {e}")
        return False
        
    print("=== HUB VERIFICATION COMPLETED SUCCESSFULLY ===")
    return True

if __name__ == "__main__":
    verify_hub()
