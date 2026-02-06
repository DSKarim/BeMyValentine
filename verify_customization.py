from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        print("Test 1: Customization via URL")
        # Go to URL with params
        url = "http://localhost:8000/index.html?title=CUSTOM_TITLE&subtitle=CUSTOM_SUBTITLE"
        page.goto(url)

        # Check H1
        h1_text = page.locator("h1").text_content()
        print(f"H1 Text: {h1_text}")
        if h1_text != "CUSTOM_TITLE":
            print("FAILURE: H1 text does not match.")
            exit(1)

        # Check Subtitle
        sub_text = page.locator(".subtitle").text_content()
        print(f"Subtitle Text: {sub_text}")
        if sub_text != "CUSTOM_SUBTITLE":
            print("FAILURE: Subtitle text does not match.")
            exit(1)

        print("Test 1 Passed.")

        print("Test 2: Admin Interface")
        # Go to clean URL
        page.goto("http://localhost:8000/index.html")

        # Click customize button
        page.click("#customize-btn")

        # Wait for modal
        page.wait_for_selector("#customization-modal", state="visible")
        print("Modal visible.")

        # Fill inputs
        page.fill("#input-title", "NEW_TITLE_FROM_MODAL")
        page.fill("#input-subtitle", "NEW_SUBTITLE")

        # Generate Link
        page.click("#modal-generate")

        # Check output
        output_value = page.input_value("#output-url")
        print(f"Generated URL: {output_value}")

        if "title=NEW_TITLE_FROM_MODAL" not in output_value:
             print("FAILURE: Generated URL missing title param.")
             exit(1)

        if "subtitle=NEW_SUBTITLE" not in output_value:
             print("FAILURE: Generated URL missing subtitle param.")
             exit(1)

        print("Test 2 Passed.")

        # Take screenshot
        page.screenshot(path="verification_customization.png")
        print("Screenshot taken.")

        browser.close()

if __name__ == "__main__":
    run()
