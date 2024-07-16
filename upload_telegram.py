import requests
import random
import telegram
import os
from dotenv import load_dotenv


def get_all_comic_number():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    all_number = response.json()["num"]
    return all_number


def loading_comment():
    filename = "python_comics.png"
    comic_num = random.randint(1, get_all_comic_number())
    url = f"https://xkcd.com/{comic_num}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comic_url = response.json()["img"]
    comic_response = requests.get(comic_url)
    comment = response.json()["alt"]
    with open(filename, "wb") as file:
        file.write(comic_response.content)
    return comment


def send_photo_auto(tg_token, chat_id, comment):
    filename = "python_comics.png"
    bot = telegram.Bot(token=tg_token)
    with open(filename, "rb") as file:
        bot.send_photo(chat_id, photo=file, caption=comment)


def main():
    load_dotenv()
    comment = loading_comment()
    tg_token = os.environ["TG_TOKEN"]
    chat_id = os.environ["CHAT_ID"]
    send_photo_auto(tg_token, chat_id, comment)
    os.remove("python_comics.png")


if __name__ == "__main__":
    main()
