import requests
from bs4 import BeautifulSoup


def urls() -> list:
    return [
        "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8346898&Area=search&mdiv=403&oid=1_2&cid=index&kw=%E6%95%B8%E6%93%9A"
    ]


def request(url: str) -> str:
    headers = {
        'authority': 'ecapi-cdn.pchome.com.tw',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)

    return response.text


def parse(response: str) -> int:
    soup = BeautifulSoup(response, 'html.parser')

    max_value = max(
        int(option['value']) for option in soup.select('select#count option'))

    return max_value
