import requests
import telepot
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
def send_photo(date, explanation):
    api_bot = os.environ.get("api_bot")
    chat_id = os.environ.get("user_id")
    bot = telepot.Bot(api_bot)
    bot.sendMessage(chat_id, date)
    bot.sendMessage(chat_id, explanation)
    bot.sendDocument(chat_id, open("nasa_daily_photo.png", "rb"))


api = os.environ.get("api_telegram")
r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api}")
photo_url = r.json()["hdurl"]
explanation = r.json()["explanation"]
photo = requests.get(photo_url)
print("Pobieranie zdjęcia")
with open("nasa_daily_photo.png", "wb") as f:
    f.write(photo.content)
date = r.json()["date"]
print("wysyłanie zdjęcia.")
send_photo(date, explanation)
os.remove("nasa_daily_photo.png")
