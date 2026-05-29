from playwright.sync_api import Page, expect
def test_customer_delete(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    page.locator("//input[@name='username']").fill("pgudi")
    page.locator("input[name='password']").fill("pgudi")
    page.locator("//button[normalize-space()='Sign In']").click()
    page.wait_for_timeout(3000)
    page.locator("//a[normalize-space()='Customers']").click()
    page.wait_for_timeout(1000)
    page.locator("//a[normalize-space()='Add Customer']").click()
    page.wait_for_timeout(1000)
    page.locator("//input[@placeholder='Enter Customer Name']").fill("auto_customer01")
    page.locator("input[placeholder='Enter EmailId']").fill("aucust@sg.com")
    page.locator("input[placeholder='Enter Location']").fill("Dallas")
    page.locator("input[placeholder='Enter Description']").fill("Testing Purpose")
    page.wait_for_timeout(1000)
    page.locator("//button[normalize-space()='Save']").click()
    page.wait_for_timeout(3000)

    def handle_alert(dialog):
        message=dialog.message
        print("Alert Message :",message)
        dialog.accept()

    page.on("dialog", handle_alert)

    page.locator("//td[text()='auto_customer01']/following-sibling::td/following-sibling::td/following-sibling::td/following-sibling::td/button[2]").click()
    page.wait_for_timeout(3000)