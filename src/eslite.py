import requests
from urllib.parse import urlparse
import json


def urls() -> list:
    return [
        'https://www.eslite.com/product/10052264232682446885007',
        'https://www.eslite.com/product/10052264232682447027000',
        'https://www.eslite.com/product/10052264232682446996000',
        'https://www.eslite.com/product/10052264232682446986001',
        'https://www.eslite.com/product/10052264232682447001000',
        'https://www.eslite.com/product/10052264232682446986001'
    ]


def request(url: str) -> str:
    parsed_url = urlparse(url)
    id = parsed_url.path.split('/')[-1]

    headers = {
        'authority': 'athena.eslite.com',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    api_url = f"https://athena.eslite.com/api/v1/products/{id}"
    response = requests.get(api_url, headers=headers)

    return response.text


def parse(response: str) -> int:
    data_json = json.loads(response)

    return int(data_json["stock"])

