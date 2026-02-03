from playwright.sync_api import sync_playwright
import time
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/index.html")

        # Wait for page to load
        page.wait_for_selector("#no-button")

        # Take initial screenshot
        page.screenshot(path="step1_initial.png")
        print("Initial screenshot taken.")

        # Hover over the button to make it move
        no_btn = page.locator("#no-button")
        initial_box = no_btn.bounding_box()
        print(f"Initial Position: {initial_box}")

        # Hover
        no_btn.hover()
        time.sleep(1) # Wait for animation

        # Take second screenshot
        page.screenshot(path="step2_moved.png")
        print("Moved screenshot taken.")

        # Check text content
        text = no_btn.text_content()
        print(f"Button text: {text}")

        if text == "Pas question":
            print("Warning: Text did not change (or random picked the same text).")
        else:
            print("Success: Text changed.")

        # Hover again to check subsequent moves
        # We need to find where it went. Playwright locator finds it by ID, so it tracks the element.
        new_box = no_btn.bounding_box()
        print(f"New Position: {new_box}")

        if new_box['x'] != initial_box['x'] or new_box['y'] != initial_box['y']:
             print("Success: Button moved.")
        else:
             print("Failure: Button did not move.")

        # Hover again
        no_btn.hover()
        time.sleep(1)
        page.screenshot(path="step3_moved_again.png")
        print("Moved again screenshot taken.")

        browser.close()

if __name__ == "__main__":
    run()
