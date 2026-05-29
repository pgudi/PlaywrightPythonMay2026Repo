from playwright.sync_api import Page, expect

def test_absolute_xpath(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=/html/body/div/form/input").first.fill("demoUser1")
    page.wait_for_timeout(1000)

def test_relative_tagnamealone(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input").first.fill("demoUser2")
    page.wait_for_timeout(1000)

def test_relative_tagnameindex(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input[2]").first.fill("demoUser3")
    page.wait_for_timeout(1000)

def test_relative_tagnameattributenamevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    osubitBtn=page.locator("xpath=//input[@type='button']")
    expect(osubitBtn).to_be_visible()
    page.wait_for_timeout(1000)

def test_relative_attributenamevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    osubitBtn=page.locator("xpath=//*[@type='button']")
    expect(osubitBtn).to_be_visible()
    page.wait_for_timeout(1000)

def test_relative_attributevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    osubitBtn=page.locator("xpath=//*[@*='button']")
    expect(osubitBtn).to_be_visible()
    page.wait_for_timeout(1000)

def test_relative_multipleattributenamevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("//input[@type='text'][@name='pass1word1']").fill("welcome123")
    page.wait_for_timeout(1000)

def test_relative_multipleattributenamevalueusingandoperator(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("//input[@type='text' and @name='pass1word1']").fill("welcome456")
    page.wait_for_timeout(1000)

def test_relative_partialattributevalue(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//input[starts-with(@id,'chk1')]").click()
    page.wait_for_timeout(2000)

def test_relative_multipleelementsmatching(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    otextfield=page.locator("xpath=//input")
    otextfield.nth(1).fill("Second Text Field")
    page.wait_for_timeout(1000)

# Find number of links in the application
def test_relative_multiplelinksmatching(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    olinks=page.locator("xpath=//a[@href]")
    print("Number of Links in Application :", olinks.count())
    page.wait_for_timeout(1000)

# display links names in the application
def test_relative_displayalllinknames(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    olinks=page.locator("xpath=//a[@href]")
    for i in range(0,olinks.count()):
        print(olinks.nth(i).text_content())
    page.wait_for_timeout(1000)

# How click on S G Software link in the application
def test_relative_clickonspecificlink(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    olinks=page.locator("xpath=//a[@href]")
    for i in range(0,olinks.count()):
         if(olinks.nth(i).text_content().startswith("S G Soft")):
            olinks.nth(i).click()
    page.wait_for_timeout(3000)

def test_relative_basedontextcontent(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//a[text()='S G Software Testing']").click()
    page.wait_for_timeout(3000)

def test_relative_basedonpartialtextcontent(page:Page):
    page.goto("file:///C:/AutomationBackupFolders/Demo/Sample.html")
    page.wait_for_timeout(2000)
    page.locator("xpath=//a[contains(text(),'Software')]").click()
    page.wait_for_timeout(3000)



