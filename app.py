import os
import requests
import configparser


def get_path(folder: str) -> str:
    """
    return a path where the project is running + folder.
    :param folder: the folder in the source tree desired.
    :return the path where the project is running and the folder desired
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), folder))


class TelegramMessager:
    def __init__(self, token: str, telegram_chat_id: int):
        self.token = token
        self.telegram_chat_id = telegram_chat_id

    def send_message(self, message: str):
        """
        send a message to a chat.
        """
        url = f"https://api.telegram.org/bot{self.token}/" \
              f"sendMessage?chat_id={self.telegram_chat_id}&text={message}"
        requests.get(url)


def check_web(url: str) -> bool:
    """
    check an url
    :parameter url: the url which I want to check
    :return bool
    """
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False


if __name__ == "__main__":
    config = configparser.ConfigParser()
    path = get_path(".")
    config.read(f"{path}/settings.ini")
    print(f"running watchmen...")
    url = config['DEFAULT']['URL']
    if check_web(url):
        print(f"URL CHECKED : -> {url}\nALL THINGS ARE RUNNIN [OK]"
              f"Grab a coffe and enjoy your day")
        telegram_messager = TelegramMessager(
            config["DEFAULT"]["TELEGRAM_BOT_TOKEN"],
            config["DEFAULT"]["TELEGRAM_CHAT_ID"])
        telegram_messager.send_message(
            f"URL CHECKED : -> {url}\n"
            f"ALL THINGS ARE RUNNIN [OK]. Grab a coffe and enjoy your day")

    else:
        print(f"Well we have an error here. Check it as soon as possible")
