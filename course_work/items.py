from datetime import datetime


class ExchangeItem:

    def __init__(self, exchange_name, currency_from, currency_to, created, changed, buy, sell) -> None:
        self.exchange_name = exchange_name
        self.currency_from = currency_from
        self.currency_to = currency_to
        self.created = created
        self.changed = changed
        self.buy = buy
        self.sell = sell

    def get_kwargs(self):
        # return {"exchange_name": self.exchange_name,
        #         "currency_from": self.currency_from,
        #         "currency_to":}
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_") and not callable(getattr(self, k))}

#
# some_exchange = ExchangeItem(exchange_name="Poloniex", currency_from="USDT", currency_to="BTC", created=datetime.now(),
#                              changed=datetime.now(), buy=4001.13, sell=4007.37)
# print(ExchangeItem.exchange_arguments)
