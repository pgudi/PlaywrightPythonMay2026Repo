
from playwright.sync_api import Page, expect

def test_launch(page:Page):
    page.goto("https://sgtestinginstituteapp.onrender.com/")
    page.wait_for_timeout(3000)
    #Capture URL and Title
    url=page.url
    print("URL of Application :",url)
    title=page.title()
    print("Title of Application :",title)
