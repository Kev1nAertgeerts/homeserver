import requests
from bs4 import BeautifulSoup

URL = r"https://www.verbi-italiani.info/nl/vervoeging/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Referer": "https://www.google.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Luanguage": "nl-BE,nl;q=0.9,es-BE;q=0.8,es;q=0.7,pt-BE;q=0.6,pt;q=0.5,nl-NL;q=0.4,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",  # br erbij is iet slecht
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Dest": "document",
    "Upgrade-Insecure-Requests": "1"
}

class Scraper:
    def __init__(self, base_url, headers):
        self.BASE_URL = base_url
        self.headers = headers
        self.statuscode = int()
        self.response = None

    def Scrape_base(self, verb_number):
        self.dic_tijden = {}
        self.response = requests.get(url=f"{self.BASE_URL}{verb_number}", headers=self.headers)
        self.statuscode = self.response.status_code
        if self.response.status_code == 200:
            soup = BeautifulSoup(self.response.text, "html.parser")
            main = soup.find("div", f"verb-conjugation-table verb-{verb_number}")
            vervoeging_list = main.find_all("div", "col-lg-6")
            for i in range(4):
                tijd = vervoeging_list[i]
                title = tijd.find("h3")
                if title == None:
                    title = tijd.find("h2")
                self.dic_tijden[title.text] = tijd

    def Specifieke_tijd(self, tijd):
        if self.statuscode == 200:
            specifiek_tijd = self.dic_tijden[tijd]
            spans = specifiek_tijd.find_all("span", "conjugation-3")
            if len(spans) == 0:
                spans = specifiek_tijd.find_all("span", "conjugation-1")
            for i in spans:
                yield i.text

    def Zoek_eerste_ww(self):
        num = 0
        while True:
            r = requests.get(url=f"{URL}{num}")
            if r.status_code == 200:
                print(f"eerste nummer: {num}")
                break
            else:
                print(f"failed num: {num}")
                num += 1
    
if __name__ == "__main__":
    scraper = Scraper(base_url=URL, headers=HEADERS)
    scraper.Scrape_base(96)
    vervoeging = scraper.Specifieke_tijd("Tegenwoordige tijd")
    #print(scraper.response.request.headers)