import time
from playwright.sync_api import sync_playwright

# Configuration
LOGIN_ID = "naveennoni2429@gmail.com"
PASSWORD = "Github@0310"
USER = "naveenjupeta"
REPO_NAME = "codegenup"
FOLDER_1 = "output"
FOLDER_2 = "programs"
FILE_NAME = ["add_to_zero.java"]

# Screenshot directory
screens_dir = "screenshots"
os.makedirs(screens_dir, exist_ok=True)

def snap(page, name: str):
    path = os.path.join(screens_dir, f"{name}.png")
    page.screenshot(path=path)
    print(f"📸 {path}")

def click_item(page, name: str, is_folder: bool):
    try:
        locator = f"//a[contains(@class,'js-navigation-open') and normalize-space(text())='{name}']"
        el = page.wait_for_selector(locator, state="visible")
        el.scroll_into_view_if_needed()
        el.click()
        target = '/tree/' if is_folder else '/blob/'
        page.wait_for_url(f"**{target}**{name}**")
        snap(page, f"opened_{name}")
        print(f"Opened {name}")
        return True
    except Exception:
        return False

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 1280, "height": 800})

    try:
        # Step 1: Login
        page.goto("https://github.com/login")
        snap(page, "login_page")
        page.fill("#login_field", LOGIN_ID)
        page.fill("#password", PASSWORD)
        snap(page, "before_submit")
        page.click("input[name='commit']")

        # Step 1a: 2FA if prompted
        try:
            otp = page.wait_for_selector("#otp", timeout=1000)
            code = input("Enter 2FA code: ")
            page.fill("#otp", code)
            page.click("//button[contains(text(), 'Verify')]")
            snap(page, "2fa_done")
        except Exception:
            pass

        page.wait_for_selector("img.avatar-user")
        print("Logged in")

        # Step 2: Open repository
        repo_url = f"https://github.com/{USER}/{REPO_NAME}"
        page.goto(repo_url)
        snap(page, "repo_home")
        time.sleep(2)

        # Step 3: Navigate to src
        if not click_item(page, FOLDER_1, True):
            page.goto(f"{repo_url}/tree/main/{FOLDER_1}")
            snap(page, FOLDER_1)
            time.sleep(2)

        # Step 4: Navigate nested path segments
        current_url = page.url
        for part in FOLDER_2.split('/'):
            if not click_item(page, part, True):
                page.goto(f"{current_url}/{part}")
                snap(page, FOLDER_2)
                time.sleep(2)
            current_url = page.url

        # Step 5: Download target files
        for fname in FILE_NAME:
            if not click_item(page, fname, False):
                page.goto(f"{current_url}/{fname}")
                time.sleep(2)
            snap(page, f"view_{fname}")
            raw_btn = page.wait_for_selector("#raw-url")
            page.goto(raw_btn.get_attribute("href"))
            content = page.inner_text("pre")
            os.makedirs("downloaded_files", exist_ok=True)
            local_path = os.path.join("downloaded_files", fname)
            with open(local_path, "w", encoding="utf-8") as f:
                f.write(content)
            snap(page, f"saved_{fname}")
            print(f"Saved {fname}")
            page.goto(current_url)
            snap(page, FILE_NAME)
            time.sleep(1)

    except Exception as e:
        print("Error occurred:", e)
        snap(page, "error")
        with open("error_page_source.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        print("Page source saved to error_page_source.html")

    finally:
        time.sleep(2)