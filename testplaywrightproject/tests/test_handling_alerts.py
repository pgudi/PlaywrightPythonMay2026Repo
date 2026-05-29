from playwright.sync_api import Page, expect

def test_simplealert(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_timeout(2000)

    def handle_alert(dialog):
        message=dialog.message
        print("Alert Content:",message)
        dialog.accept()

    page.on("dialog", handle_alert)
    
    page.locator("//button[text()='Click for JS Alert']").click()
    page.wait_for_timeout(1000)
    print(page.locator("//p[@id='result']").text_content())
    page.wait_for_timeout(2000)

def test_confirmalert(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_timeout(2000)

    def handle_alert(dialog):
        message=dialog.message
        print("Alert Content:",message)
        dialog.accept()

    page.on("dialog", handle_alert)
    
    page.locator("//button[text()='Click for JS Confirm']").click()
    page.wait_for_timeout(1000)
    print(page.locator("//p[@id='result']").text_content())
    page.wait_for_timeout(2000)

def test_promptalert(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_timeout(2000)

    def handle_alert(dialog):
        message=dialog.message
        print("Alert Content:",message)
        dialog.accept("WELCOME PLAYWRIGHT")

    page.on("dialog", handle_alert)
    
    page.locator("//button[text()='Click for JS Prompt']").click()
    page.wait_for_timeout(1000)
    print(page.locator("//p[@id='result']").text_content())
    page.wait_for_timeout(2000)