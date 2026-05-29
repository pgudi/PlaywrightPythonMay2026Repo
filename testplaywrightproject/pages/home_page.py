
from playwright.sync_api import Page

class HomePage:
    def __init__(self,page:Page):
        self.page=page
        self.logout=page.locator("//button[normalize-space()='Logout']")

    def clcik_logout(self):
        self.logout.click()