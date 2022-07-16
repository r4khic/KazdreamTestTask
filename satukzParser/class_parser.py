import requests
import json
from bs4 import BeautifulSoup


class SatukzParser:

    @staticmethod
    def get_request(url):
        try:
            headers = {
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/53.0.2785.116 '
                              'Safari/537.36 OPR/40.0.2308.81',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'DNT': '1',
                'Accept-Encoding': 'gzip, deflate, lzma, sdch',
                'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
            }
            req = requests.get(url, headers=headers)
            result = req.text
        except requests.RequestException:
            return None
        return result

    @staticmethod
    def get_links(page):
        links = []
        soup = BeautifulSoup(page, "lxml")
        elements = soup.findAll('loc')
        items_links = list(dict.fromkeys(elements))  # to remove duplicate links
        for item_link in items_links:
            if "smartfony/" in item_link.text or "catalog/" in item_link.text or "offer/smart-chasy-" in item_link.text or "/smart-chasy/" in item_link.text:
                continue
            if "knopochnye-telefony/" in item_link.text or "fitnes-braslety-remeshki/" in item_link.text:
                continue
            links.append(item_link.text)
        return links

    def parse_item(self, page):
        soup = BeautifulSoup(page, "html.parser")
        element = soup.find('script', {'type': 'application/ld+json'}).text
        data = json.loads(element)
        name = data['name']
        articul = data['mpn']
        price = data['offers']['price']
        item_mem = self.parse_item_memory(soup)
        data = {
            "name": name,
            "articul": articul,
            "price": price,
            "memory-size": item_mem,
        }
        return data

    def parse_item_memory(self, page):
        element = None
        top_tag = 'Объем встроенной памяти: '
        bottom_tag = '</li>'
        str_page = str(page)
        top_tag_position = str_page.find(top_tag)
        if top_tag_position != -1:
            top_tag_position += len(top_tag)
            element = str_page[top_tag_position:]
            bottom_tag_position = element.find(bottom_tag)
            if bottom_tag_position != -1:
                element = element[:bottom_tag_position]
        return element

    def write_data(self, data):
        out_file = open("smartphones.json", "w")
        json.dump(data, out_file)
        out_file.close()
