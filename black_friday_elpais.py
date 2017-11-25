import cookielib
import urllib3
import requests
from bs4 import BeautifulSoup
from collections import Counter

def process_page(p):
    s = requests.Session()
    url = "https://elpais.com/buscador/?qt=%22black+friday%22&sf=1&np={}&bu=ep&of=html".format(p)
    s.get("https://www.elpais.com") # set cookies
    data = s.get(url).text
    parser = BeautifulSoup(data)
    dates = [x.text.split("/")[2] for x in parser.find_all("span", {"class": "fecha"})]
    return dates

if __name__ == "__main__":

    pages = range(16)
    dates = []
    for p in pages:
        print "Getting page {}".format(p)
        d = process_page(p)
        dates.extend(d)

    c = Counter(dates)
    print c

