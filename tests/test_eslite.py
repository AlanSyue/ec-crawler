import src.eslite as eslite
from tests.helpers.files_helper import read_file

IN_STOCK_DATA_FILE = 'tests/fixtures/eslite/in_stock.txt'


def test_request():
    url = "https://www.eslite.com/product/1005186222682128590007?utm=123&test=12312"
    result = eslite.request(url)

    assert type(result) is str


def test_parse():
    response = read_file(IN_STOCK_DATA_FILE)
    result = eslite.parse(response)

    assert result == 5
