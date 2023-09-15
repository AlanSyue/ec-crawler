import requests
from bs4 import BeautifulSoup


def urls() -> list:
    return [
        "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=11860072&str_category_code=2104400333&sourcePageType=4",
        "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=11857489&str_category_code=2104400333&sourcePageType=4",
        "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=11854641&str_category_code=2104400333&sourcePageType=4",
        "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=11854643&str_category_code=2104400333&sourcePageType=4",
        "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=11854650&str_category_code=2104400333&sourcePageType=4",
        "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=11854639&str_category_code=2104400332&sourcePageType=4",
        "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=11854635&str_category_code=2104400332&sourcePageType=4"
    ]


def request(url: str) -> str:
    headers = {
        'authority': 'www.momoshop.com.tw',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)

    return response.text


def parse(response: str) -> int:
    soup = BeautifulSoup(response, 'html.parser')
    element = soup.find(id='buy_yes')

    is_for_sale = True
    if element and 'style' in element.attrs and 'display:none' in element.attrs['style']:
        is_for_sale = False

    max_value = 0
    if is_for_sale:
        max_value = max(
            int(option['value']) for option in soup.select('select#count option'))
    else:
        max_value = 0

    return max_value
