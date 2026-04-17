import re
from playwright.sync_api import expect

def test_google_search(page):
    page.goto("https://www.google.com/ncr")

    try:
        page.get_by_role("button", name="I agree").click(timeout=3000)
    except:
        print("No cookie consent button found, proceeding with the test.")

    search = page.get_by_role("combobox", name="Search")
    search.fill("Playwright Python")
    search.press("Enter")

    page.wait_for_load_state("networkidle")

    # Better assertion (more stable than title)
    expect(page).to_have_url(re.compile("q=Playwright", re.IGNORECASE))