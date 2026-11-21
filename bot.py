
import os
import json
import urllib.request

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = "@fantom_bek"

posts = [
    "🌍 EVERY DAY\n\n💡 Har kuni yangi bilim olish — kelajak sari qadam!\n\n#EveryDay #Motivatsiya",
    "🧠 QIZIQARLI FAKT\n\nAsalarilar bir-biriga raqs orqali oziq-ovqat manzilini bildira oladi!\n\n#Fakt #EveryDay",
    "🚀 TEXNOLOGIYA\n\nSun'iy intellekt kundalik hayotimizni o'zgartirmoqda!\n\n#IT #EveryDay"
]

def send_post(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = json.dumps({
        "chat_id": CHANNEL,
        "text": message
    }).encode()

    req = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(req) as response:
        print(response.read().decode())

send_post(posts[0])
