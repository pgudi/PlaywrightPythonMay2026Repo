from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        self.username=page.locator("//input[@name='username']")
        self.password=page.locator("//input[@name='password']")
        self.btnsignin=page.locator("//button[normalize-space()='Sign In']")

    def set_username(self,username):
        self.username.fill(username)

    def set_password(self,password):
        self.password.fill(password)

    def click_signin(self):
        self.btnsignin.click()
