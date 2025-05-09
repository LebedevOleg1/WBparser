import re
from collections import Counter
import itertools
import requests
import urllib.parse


def get_id(url):
    return int(url.split("/")[-2])

def get_name(product_id):
    url_product_id = f"https://card.wb.ru/cards/detail?appType=1&curr=rub&dest=-1257786&spp=0&nm={product_id}"
    response = requests.get(url_product_id)
    data = response.json()
    if "data" in data and "products" in data["data"]:
        product = data["data"]["products"][0]
        return product["name"]
    else:
        return None


def extract_keywords(title):
    words = re.findall(r'\b\w+\b', title.lower())
    stopwords = {"для", "и", "в", "из", "с", "на", "по", "от", "до", "цвет", "размер", "новый", "мужской",
                 "женский"}
    keywords = [word for word in words if word not in stopwords]
    phrases = list(itertools.chain(zip(keywords, keywords[1:], keywords[2:]), zip(keywords, keywords[1:]), keywords))
    counter = Counter(phrases)
    return [" ".join(p) if isinstance(p, tuple) else p for p, _ in counter.most_common(10)]


def get_position(url, pages):
    try:
        product_id = get_id(url)
        name = get_name(product_id)
        words = extract_keywords(name)
        result = {}

        for query in words:
            flag = False
            for page in range(pages):
                encoded_query = urllib.parse.quote(query)
                search_url = f"https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&curr=rub&dest=-1257786&spp=0&query={encoded_query}&resultset=catalog&page={page}"
                response = requests.get(search_url)
                data = response.json()
                if "data" in data and "products" in data["data"]:
                    for product in range(len(data['data']['products'])):
                        if (data['data']['products'])[product]['id'] == product_id:

                            result[f'Запрос: "{query}"'] = f"Товар найден на странице {page+1}. Позиция {product+1}."
                            flag = True
                            break
                if flag:
                    break
            else:
                result[f'Запрос: "{query}"'] = "Товар не найден."
        return result
    except:
        return ValueError



