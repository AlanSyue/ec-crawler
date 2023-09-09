import requests
from urllib.parse import urlparse
import json


def urls() -> list:
    return [
        'https://24h.pchome.com.tw/prod/DYAJ88-A900FHDI4'
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
    json_str = response.split("[")[1].split("]")[0]
    data_json = json.loads(json_str)

    return int(data_json["Qty"])

