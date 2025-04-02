from playwright.sync_api import sync_playwright
import time

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
url = "https://web.whatsapp.com"
channelName = "Test"
message = "This is a test message"

#region Whatsapp Web login
playwright = sync_playwright().start()
context = playwright.chromium.launch_persistent_context(user_data_dir="./Profile", headless=False, user_agent=userAgent)
page = context.new_page()
page.goto(url)
page.get_by_label('Scan this QR code to link a device!').focus()
#page.screenshot(path="qr.png")
time.sleep(60)
context.close()
#endregion

#region Send message
playwright = sync_playwright().start()
context = playwright.chromium.launch_persistent_context(user_data_dir="./Profile", headless=False, user_agent=userAgent)
page = context.new_page()
page.goto(url)
time.sleep(10)

page.click("button[aria-label='Channels']")
time.sleep(2)

page.click(f"span[title='{channelName}']")
time.sleep(2)

page.click("div[aria-label='Type an update']")
msgField = page.get_by_label("Type an update")
msgField.fill(message)
time.sleep(2)

sendButton = page.click("button[aria-label='Send']")
time.sleep(3)

page.close()
context.close()
#endregion