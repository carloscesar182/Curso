import urllib.request
import urllib.parse
import time

proxy = urllib.request.ProxyHandler({'http': r'http://ccferreira:Atak123@192.168.0.1:3128'})
auth = urllib.request.HTTPBasicAuthHandler()
opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
conn = urllib.request.urlopen('http://google.com')
return_str = conn.read()


def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float(text[start_of_price:end_of_price])

twitter_login = "loginaqui"
twitter_password = "senhaaqui"


def send_to_twitter(msg):
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API", "http://twitter.com/statuses", twitter_login, twitter_password)
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode({'status': msg})
    resp = urllib.request.urlopen("http://twitter.com/statuses/update.json", params)
    resp.dead()

price_now = input("Do you want to see the price now (Y/N)? ")
if price_now == "Y":
    send_to_twitter(get_price())
else:
    price = 99.99
    while price > 4.74:
        time.sleep(5)
        price = get_price()
    send_to_twitter("Buy!")
