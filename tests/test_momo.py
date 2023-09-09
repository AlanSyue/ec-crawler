import src.momo as momo
from tests.helpers.files_helper import read_file

IN_STOCK_DATA_FILE = 'tests/fixtures/momo/in_stock.txt'


def test_request():
    url = 'https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8346898&Area=search&mdiv=403&oid=1_2&cid=index&kw=%E6%95%B8%E6%93%9A'
    result = momo.request(url)
 
    assert type(result) is str


def test_parse():
    response = read_file(IN_STOCK_DATA_FILE)
    result = momo.parse(response)
    assert result == 2
