from playwright.sync_api import Page, expect

def test_login_logout(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    # Perform Login Action
    page.locator("//input[@name='username']").fill("pgudi")
    page.locator("//input[@type='password']").fill("pgudi")
    page.locator("//button[text()='Sign In']").click()
    page.wait_for_timeout(3000)
    # Perform Logout Action
    page.locator("//button[text()='Logout']").click()
    page.wait_for_timeout(3000)
