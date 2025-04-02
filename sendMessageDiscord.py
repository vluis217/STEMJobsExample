import json
import requests

def sendMessageDiscord(webhookUrl, message):
    requestHeaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8"
    }

    body = {
        "content": message
    }
    body = json.dumps(body, ensure_ascii=True) #Taken from https://python-forum.io/thread-17834.html

    session = requests.Session()
    response = session.post(url=webhookUrl, headers=requestHeaders, data=body)

#Usage example:
sendMessageDiscord("https://discord.com/api/webhooks/1234567890/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "This is a test.")