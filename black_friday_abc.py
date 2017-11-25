import cookielib
import urllib3
import requests
from bs4 import BeautifulSoup
from collections import Counter

def process_page(p):
    s = requests.Session()
    url = "http://www.abc.es/hemeroteca/noticia/+black+friday/pagina-{}".format(p)
    s.get("http://www.abc.es") # set cookies
    data = s.get(url).text
    parser = BeautifulSoup(data)
    dates = [x.text.split("/")[2].split(" ")[0] for x in parser.find_all("span", {"class": "date"})]
    return dates

if __name__ == "__main__":

    pages = range(1, 40)
    dates = []
    for p in pages:
        print "Getting page {}".format(p)
        d = process_page(p)
        dates.extend(d)

    c = Counter(dates)
    print c

