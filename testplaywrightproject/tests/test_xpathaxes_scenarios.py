from playwright.sync_api import Page, expect

def test_following_sibling(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/WebTableHTML.html")
    page.wait_for_timeout(3000)
    page.locator("xpath=//td[text()='Sachin Tendulkar']/following-sibling::td/following-sibling::td/following-sibling::td/following-sibling::td/input").fill("25000")
    page.wait_for_timeout(3000)

def test_following(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/WebTableHTML.html")
    page.wait_for_timeout(3000)
    page.locator("xpath=//td[text()='Sachin Tendulkar']/following::tr[1]/td[6]/input").fill("25000")
    page.wait_for_timeout(3000)

def test_preceding_sibling(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/WebTableHTML.html")
    page.wait_for_timeout(3000)
    page.locator("xpath=//td[text()='Indian Freedom Fighter']/preceding-sibling::td[1]/preceding-sibling::td[1]/input").click()
    page.wait_for_timeout(3000)

def test_preceding(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/WebTableHTML.html")
    page.wait_for_timeout(3000)
    page.locator("xpath=//td[text()='Rahul Dravid']/preceding::tr[1]/td[1]/input").click()
    page.wait_for_timeout(3000)

def test_ancestor(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/WebTableHTML.html")
    page.wait_for_timeout(3000)
    v1=page.locator("xpath=//input[@id='edit4']/ancestor::td/ancestor::tr/ancestor::table").get_attribute("id")
    print("Tabel id Value :",v1)
    page.wait_for_timeout(3000)

def test_descendant(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/WebTableHTML.html")
    page.wait_for_timeout(3000)
    page.locator("xpath=//table[@id='tbl1']/descendant::tr[4]/td[6]/input").fill("18000")
    page.wait_for_timeout(3000)

