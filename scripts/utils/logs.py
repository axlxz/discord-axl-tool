import datetime
from scripts.utils.config import save_file

def save_log(text):
    date = datetime.datetime.now()

    date_1 = date.strftime("%Y-%m-%d")

    date_2 = date.strftime("%Y-%m-%d %H:%M:%S")

    save_file(f"./logs/{date_1}", f"{date_2} | {text}")