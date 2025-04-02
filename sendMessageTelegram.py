import json
import requests

def sendMessageTelegram(webhookUrl, chatId, message, disableEmbed=False):
    requestHeaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8"
    }

    escapeChars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for escapeChar in escapeChars:
        message = message.replace(escapeChar, f'\\{escapeChar}')

    body = {
        "chat_id": chatId,
        "parse_mode": "MarkdownV2",
        "text": message,
        "disable_web_page_preview": disableEmbed
    }
    body = json.dumps(body, ensure_ascii=True)

    session = requests.Session()
    response = session.post(url=webhookUrl, headers=requestHeaders, data=body)


#Usage example:
sendMessageTelegram("https://api.telegram.org/bot1234567890:abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ/sendMessage", "-1001234567890", "This is a test.")