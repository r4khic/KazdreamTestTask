from satukzParser.class_parser import SatukzParser
from urllib.parse import urlparse

'''В задании было сказано брать от сюда
https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/
Я посмотрел структуру сайта и обнаружил сайтмап где содержатся все товары в категории "Смартфоны" вот по этой ссылке
https://shop.kz/sitemap-iblock-45.xml'''


def main():
    parser = SatukzParser()
    items_data = []
    URL = 'https://shop.kz/sitemap-iblock-45.xml'
    web_page = parser.get_request(URL)
    item_links = parser.get_links(web_page)
    counter = 0
    for item_link in item_links:
        counter += 1
        item_page = parser.get_request(item_link)
        item_data = parser.parse_item(item_page)
        items_data.append(item_data)
    parser.write_data(items_data)


if __name__ == '__main__':
    main()
