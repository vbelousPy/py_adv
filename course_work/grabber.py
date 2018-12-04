import time
from datetime import datetime

import requests
from requests.exceptions import InvalidSchema

from course_work.database_utils import update_record


class Grabber:

    def __init__(self, exchange_list=(), currency_list=(), update_time=180) -> None:
        self.is_updating = False
        self.exchange_list = exchange_list
        self.currency_list = currency_list
        self.update_time = update_time

    def start(self):
        self.is_updating = True
        while self.is_updating:
            # print("working = " + str(datetime.now())) LOGGING
            for exchange in self.exchange_list:
                for currency in self.currency_list:
                    update_record(exchange.get_data("USD", currency.strip()))
            time.sleep(self.update_time)

    def stop(self):
        # print("stop") LOGGING
        self.is_updating = False


class BaseExchange:

    def __impl_parsing__(self, currency_from, currency_to):
        raise NotImplementedError

    def get_data(self, currency_from, currency_to):
        try:
            buy, sell = self.__impl_parsing__(currency_from, currency_to)
        except (InvalidSchema, AttributeError, ConnectionError):
            buy, sell = None, None
        current_timestamp = int(datetime.now().timestamp())
        return {"exchange_name": self.__class__.__name__,
                "currency_from": currency_from,
                "currency_to": currency_to,
                "created": current_timestamp,
                "changed": current_timestamp,
                "buy": buy,
                "sell": sell}


class Poloniex(BaseExchange):

    def __impl_parsing__(self, currency_from, currency_to):
        if currency_from == "USD".upper():
            currency_from = "USDT"
        url_api = "https://poloniex.com/public?command=returnTicker"
        result = requests.get(url_api).json().get("{}_{}".format(currency_from, currency_to))
        return result.get("highestBid"), result.get("lowestAsk")


class Bitfinex(BaseExchange):

    def __impl_parsing__(self, currency_from, currency_to):
        url_api = "https://api.bitfinex.com/v1/pubticker/{}{}".format(currency_to, currency_from)
        result = requests.get(url_api).json()
        return result.get("bid"), result.get("ask")


class Cryptex(BaseExchange):

    def __impl_parsing__(self, currency_from, currency_to):
        url_api = "https://cryptex.net/api/v1/{}_{}/ticker".format(currency_to, currency_from)
        result = requests.get(url_api).json().get("data")
        return result.get("low"), result.get("high")


class Bittrex(BaseExchange):

    def __impl_parsing__(self, currency_from, currency_to):
        if currency_from == "USD".upper():
            currency_from = "USDT"
        url_api = "https://bittrex.com/api/v1.1/public/getmarketsummary?market={}-{}".format(currency_from, currency_to)
        result = requests.get(url_api).json().get("result")[0]
        return result.get("Bid"), result.get("Ask")

