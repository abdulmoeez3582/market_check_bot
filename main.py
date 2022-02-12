import requests


def get_BTC():

    crypto_data = requests.get(
        "https://api.upbit.com/v1/ticker?markets=KRW-BTC").json()

    data = []
    for i in crypto_data:
         data = i["trade_price"]
    return data

if __name__ == "__main__":
    print(get_BTC())