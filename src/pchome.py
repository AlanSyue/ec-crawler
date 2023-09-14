import requests
from urllib.parse import urlparse
import json


def urls() -> list:
    return [
        'https://24h.pchome.com.tw/prod/DYAJDN-A900GNNGQ?fq=/S/DYAJDN',
        'https://24h.pchome.com.tw/prod/DYAJDN-A900GNO39?fq=/S/DYAJDN',
        'https://24h.pchome.com.tw/prod/DYAJDN-A900GNO4R?fq=/S/DYAJDN',
        'https://24h.pchome.com.tw/prod/DYAJDN-A900GNO68?fq=/S/DYAJDN',
        'https://24h.pchome.com.tw/prod/DYAJ8N-A900GNO75?fq=/S/DYAJ8N',
        'https://24h.pchome.com.tw/prod/DYAJ8N-A900GNO7E?fq=/S/DYAJ8N',
        'https://24h.pchome.com.tw/prod/DYAJ8N-A900GNO7N?fq=/S/DYAJ8N',
        'https://24h.pchome.com.tw/prod/DYAJ3N-A900GNNPA?fq=/S/DYAJ3N',
        'https://24h.pchome.com.tw/prod/DYAJ3N-A900GNNY3?fq=/S/DYAJ3N',
        'https://24h.pchome.com.tw/prod/DYAJ3N-A900GNO0S?fq=/S/DYAJ3N'
    ]


def request(url: str) -> str:
    parsed_url = urlparse(url)
    id = parsed_url.path.split('/')[-1]

    headers = {
        'authority': 'ecapi-cdn.pchome.com.tw',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    api_url = f"https://ecapi-cdn.pchome.com.tw/ecshop/prodapi/v2/prod/button&id={id}&fields=Qty&_callback=jsonp_button?_callback=jsonp_button"
    response = requests.get(api_url, headers=headers)

    return response.text


def parse(response: str) -> int:
    json_str = response.split("(")[1].split(")")[0]
    data_json = json.loads(json_str)

    return sum(item["Qty"] for item in data_json)

