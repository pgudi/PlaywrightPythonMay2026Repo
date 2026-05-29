from playwright.sync_api import Page, expect

def test_absolute_css(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=html body div form input").first.fill("demoUser1")
    page.wait_for_timeout(1000)

def test_relative_tagname(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input").first.fill("demoUser1")
    page.wait_for_timeout(1000)

def test_relative_tagnamewithidattributevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input#pwd1pass1word1").fill("Welcome1234")
    page.wait_for_timeout(1000)

def test_relative_idattributevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=#pwd1pass1word1").fill("Welcome1")
    page.wait_for_timeout(1000)

def test_relative_tagnamewithclassattributevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input.pass1word1").fill("HelloWorld")
    page.wait_for_timeout(1000)

def test_relative_classattributevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=.pass1word1").fill("SayHello123")
    page.wait_for_timeout(1000)

def test_relative_tagnamewithattributenameandvalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input[name='windows']").click()
    page.wait_for_timeout(1000)

def test_relative_tagnamewithmultipleattributenameandvalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input[type='checkbox'][name='linus']").click()
    page.wait_for_timeout(1000)

def test_relative_partialmatchingofattributevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("css=input[id *= 'fire']").click()
    page.wait_for_timeout(2000)

# Numbe of links in the application
def test_relative_multipleelementsmatching(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    olinks=page.locator("css=a[href]")
    print("Number of Links are :",olinks.count())
    page.wait_for_timeout(2000)

# Display All Links in the application
def test_relative_displaylinknames(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    olinks=page.locator("css=a[href]")
    for i in range(0,olinks.count()):
        print(olinks.nth(i).text_content())
    page.wait_for_timeout(2000)

# Click on specific link in  the application
def test_relative_specificlink(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    olinks=page.locator("css=a[href]")
    for i in range(0,olinks.count()):
        if olinks.nth(i).text_content().startswith("S G"):
            olinks.nth(i).click()
            break
    page.wait_for_timeout(2000)