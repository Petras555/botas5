import random
import subprocess
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import sys


# def ensure_playwright_browsers():
#     """Checks if Chromium is installed; if not, installs it."""
#     print("Checking for browser dependencies...")
#     try:
#         # This command returns 0 if chromium is installed
#         subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
#         print("Browser check complete.")
#     except Exception as e:
#         print(f"Error installing browsers: {e}")

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

def run(playwright: Playwright) -> None:
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
        minutes = random.randint(1, 3)  # whole minutes
        print(f"Sleeping for {minutes} minutes...")
        time.sleep(minutes * 60)
    

    # page.click("text=More information")

    # # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
