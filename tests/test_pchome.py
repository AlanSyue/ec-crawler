import src.pchome as pchome

OUT_OF_STOCK_DATA = {
    "response": 'try{jsonp_button([{"Qty":0},{"Qty":0},{"Qty":0},{"Qty":0},{"Qty":0}]);}catch(e){if(window.console){console.log(e);}}'
}

NOT_READY_DATA = {
    "response": 'try{jsonp_button([{"Qty":1,"ButtonType":"NotReady"},{"Qty":1,"ButtonType":"NotReady"},{"Qty":1,"ButtonType":"NotReady"},{"Qty":1,"ButtonType":"NotReady"},{"Qty":1,"ButtonType":"NotReady"}]);}catch(e){if(window.console){console.log(e);}}'
}

IN_STOCK_DATA = {
    "response": 'try{jsonp_button([{"Qty":20},{"Qty":0},{"Qty":0},{"Qty":0},{"Qty":0}]);}catch(e){if(window.console){console.log(e);}}'
}


def test_parse():
    result = pchome.parse(OUT_OF_STOCK_DATA["response"])
    assert result == 0


def test_parse_not_ready():
    result = pchome.parse(NOT_READY_DATA["response"])
    assert result == 0


def test_parse_in_stock():
    result = pchome.parse(IN_STOCK_DATA["response"])
    assert result == 20


def test_request():
    url = "https://24h.pchome.com.tw/prod/DHAFPP-1900GGI89"
    result = pchome.request(url)

    assert result == 'try{jsonp_button([{"Qty":20}]);}catch(e){if(window.console){console.log(e);}}'
