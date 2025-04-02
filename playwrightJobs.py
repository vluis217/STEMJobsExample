from playwright.sync_api import sync_playwright

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

url = "https://www.google.com/about/careers/applications/jobs/results/"

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=True)

context = browser.new_context(user_agent=userAgent)

page = context.new_page()

page.goto(url)

page.click('h3:has-text("Locations")')

page.fill('input[aria-label="Which location(s) do you prefer working out of?"]', "Colombia")

page.click('li[data-suggestion-id="Colombia"]')

page.wait_for_selector('.sMn82b')

jobs = page.query_selector_all('.sMn82b')

for job in jobs:
    print(f"ID: {job.query_selector('a').get_attribute('href').split("/")[2].split("-")[0]}")
    print(f"Título: {job.query_selector('h3').text_content()}")
    print(f"Empresa: {job.query_selector('.RP7SMd').query_selector('span').text_content()}")
    print(f"Nivel de experiencia: {job.query_selector('.wVSTAb').text_content()}")
    print(f"Ubicación: {job.query_selector('.r0wTof').text_content()}")
    print(f"Link: https://www.google.com/about/careers/applications/{job.query_selector('a').get_attribute('href')}")
    print()

browser.close()
