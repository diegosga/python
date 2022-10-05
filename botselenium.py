from multiprocessing.connection import wait
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 browser = p.chromium.launch(headless=False)
 page = browser.new_page()
 page.goto("https://www.youtube.com/watch?v=NSxVV9hwJKo")
 page.click("span[id='video-title']")
 page.wait_for_timeout(10000000)
