import random
import subprocess
import os
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import sys


def ensure_browsers():
    """Checks for Chromium; installs it if missing."""
    print("Step 1: Ziuri NX...")
    try:
        # We use the internal playwright module to run the install command
        # This works even inside a PyInstaller EXE
        subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
        print("Pavyko Nx.")
    except Exception as e:
        print(f"Warning: Automatic browser install failed: {e}")
        print("The bot will try to continue, but may crash if Chromium is missing.")

def random_delay(min_ms=200, max_ms=1000):
    """Sleep for a random interval between min_ms and max_ms milliseconds"""
    time.sleep(random.uniform(min_ms, max_ms) / 1000)


def ferma1(page):
    page.get_by_role("link").nth(3).click()
    random_delay(500, 1500)
    page.get_by_role("textbox", name="X:").click()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").click()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").type("118", delay=100)
    random_delay(300, 1200)
    page.get_by_role("textbox", name="Y:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="Y:").type("112", delay=120)
    random_delay(300, 1200)
    page.get_by_role("button", name="OK").click()
    random_delay(300, 1200)
    page.locator("#mapContainer > div > div:nth-child(2)").first.click()
    random_delay(300, 1200)
    page.get_by_role("link", name="Send troops", exact=True).click()
    random_delay(300, 1200)
    page.locator("input[name=\"troop[t5]\"]").click()
    random_delay(300, 1200)
    page.locator("input[name=\"troop[t5]\"]").type("10")
    random_delay(300, 1200)
    page.get_by_role("button", name="Send").click()
    random_delay(300, 1200)
    page.get_by_role("button", name="Confirm").click()
    random_delay(300, 1200)
    print("yra ataka")

def ferma2(page):
    page.get_by_role("link").nth(3).click()
    page.get_by_role("textbox", name="X:").click()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").click()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").type("117", delay=130)
    random_delay(300, 1200)
    page.get_by_role("textbox", name="Y:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="Y:").type("109", delay=160)
    random_delay(300, 1200)
    page.get_by_role("button", name="OK").click()
    random_delay(300, 1200)
    page.locator("#mapContainer > div > div:nth-child(2)").first.click()
    random_delay(300, 1200)
    page.get_by_role("link", name="Send troops", exact=True).click()
    random_delay(300, 1200)
    page.locator("input[name=\"troop[t5]\"]").click()
    random_delay(300, 1200)
    page.locator("input[name=\"troop[t5]\"]").click()
    random_delay(300, 1200)
    page.locator("input[name=\"troop[t5]\"]").type("10")
    random_delay(300, 1200)
    page.get_by_role("button", name="Send").click()
    random_delay(300, 1200)
    page.get_by_role("button", name="Confirm").click()
    random_delay(300, 1200)
    print("yra ataka")

def ferma3(page):
    page.get_by_role("link").nth(3).click()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").click()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").click()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").type("120", delay=140)
    random_delay(300, 1200)
    page.get_by_role("textbox", name="Y:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="Y:").type("109", delay=170)
    random_delay(300, 1200)
    page.get_by_role("button", name="OK").click()
    random_delay(300, 1200)
    page.locator("#mapContainer > div > div:nth-child(2)").first.click()
    random_delay(300, 1200)
    page.get_by_role("link", name="Send troops", exact=True).click()
    random_delay(300, 1200)
    page.locator("input[name=\"troop[t5]\"]").click()
    random_delay(300, 1200)
    page.locator("input[name=\"troop[t5]\"]").click()
    random_delay(300, 1200)
    page.locator("input[name=\"troop[t5]\"]").type("10")
    random_delay(300, 1200)
    page.get_by_role("button", name="Send").click()
    random_delay(300, 1200)
    page.get_by_role("button", name="Confirm").click()
    random_delay(300, 1200)
    print("yra ataka")

def ferma4(page):
    page.get_by_role("link").nth(3).click()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").click()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").click()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="X:").type("115", delay=140)
    random_delay(300, 1200)
    page.get_by_role("textbox", name="Y:").dblclick()
    random_delay(300, 1200)
    page.get_by_role("textbox", name="Y:").type("119", delay=120)
    random_delay(300, 1200)
    page.get_by_role("button", name="OK").click()
    random_delay(300, 1200)
    page.locator("#mapContainer > div > div:nth-child(2)").first.click()
    random_delay(300, 1200)
    page.get_by_role("link", name="Send troops", exact=True).click()
    random_delay(300, 1200)
    page.locator("input[name=\"troop[t5]\"]").click()
    random_delay(300, 1200)
    page.locator("input[name=\"troop[t5]\"]").click()
    random_delay(300, 1200)
    page.locator("input[name=\"troop[t5]\"]").type("10")
    random_delay(300, 1200)
    page.get_by_role("button", name="Send").click()
    
    random_delay(300, 1200)
    page.get_by_role("button", name="Confirm").click()
    random_delay(300, 1200)
    print("yra ataka")


actions = [ferma1, ferma2, ferma3, ferma4]


def ataka(page):
    random.shuffle(actions)
    for func in actions:
        func()

def run_bot(playwright: Playwright) -> None:
    print("Step 2: Jungiam browseri nx...")
    try:
        browser = playwright.chromium.launch(headless=False, slow_mo=350)
        context = browser.new_context()
        
        page = context.new_page()
        page.goto("https://www.travian.com/international")
        page.get_by_role("button", name="Login").click()
        
        random_delay(300, 1200)
        page.get_by_role("textbox", name="Enter your email address or").click()
        random_delay(300, 1200)
        page.get_by_role("textbox", name="Enter your email address or").type("jslionskis@gmail.com", delay=100)
        page.get_by_role("textbox", name="Enter your password:").click()
        random_delay(300, 1200)
        page.get_by_role("textbox", name="Enter your password:").type("Travian3911", delay=130)
        page.locator("#loginLobby").get_by_role("button", name="Login").click()
        
        random_delay(300, 1200)
        page.get_by_role("button", name="Play now").click()
        random_delay(300, 1200)

        while True:
            random.shuffle(actions)
            for func in actions:
                func(page)
            minutes = random.randint(17, 22)  # whole minutes
            print(f"Sleeping for {minutes} minutes...")
            time.sleep(minutes * 60)
    except Exception as e:
        print(f"Critical error: {e}")
        input("Press Enter to close...")

    # page.click("text=More information")

    # # ---------------------
    # context.close()
    # browser.close()

# git status
# git add .
# git commit -m "Initial commit"
# git branch -M main
# git push --set-upstream origin main


if __name__ == "__main__":
    ensure_browsers()
    with sync_playwright() as playwright:
        run_bot(playwright)