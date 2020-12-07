import requests
import configparser

def check_web(url):
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
    config  = configparser.ConfigParser()
    config.read('settings.ini')
    print(f"running watchmen...")
    url = config['DEFAULT']['URL']
    if check_web(url):
        print(f"URL CHECKED : -> {url}\nALL THINGS ARE RUNNIN [OK]. Grab a coffe and enjoy your day")
    else:
        print(f"Well we have an error here. Check it as soon as possible")
