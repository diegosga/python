from playwright.sync_api import sync_playwright
from multiprocessing.connection import wait
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://twitter.com/i/flow/login")
    page.fill("input[name='text']","digascongelado")
    page.click("div[dir='auto']")
    page.fill("input[name='password']","rukiddingme1")
    page.click("div[role='button']")