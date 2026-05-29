from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login_logout(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    # Create object for LoginPage, HomePage
    login=LoginPage(page)
    home=HomePage(page)
    #Login Action
    login.set_username("pgudi")
    login.set_password("pgudi")
    login.click_signin()
    page.wait_for_timeout(3000)
    home.clcik_logout()
    page.wait_for_timeout(3000)
