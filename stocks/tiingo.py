import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 6350cd534f3a0a4694e12e8c7fe50aa2d513806c',
}


def get_meta_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()


def get_price_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}/prices".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()[0]    
    