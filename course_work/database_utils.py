from peewee import *


database = MySQLDatabase("local_database", user='root', password='copermine', host='127.0.0.1', port=3306)


class BaseModel(Model):
    class Meta:
        database = database


class ExchangeRate(BaseModel):
    id = BigAutoField()
    exchange_name = CharField()
    currency_from = CharField()
    currency_to = CharField()
    created = BigIntegerField()
    changed = BigIntegerField()
    buy = FloatField()
    sell = FloatField()


def update_record(exchange_kwargs):
    try:
        # print("exchange = " + str(exchange_kwargs))
        result = ExchangeRate \
            .update({ExchangeRate.changed: exchange_kwargs.get("changed"), ExchangeRate.buy: exchange_kwargs.get("buy"),
                     ExchangeRate.sell: exchange_kwargs.get("sell")}) \
            .where(ExchangeRate.exchange_name == exchange_kwargs.get("exchange_name"),
                   ExchangeRate.currency_from == exchange_kwargs.get("currency_from"),
                   ExchangeRate.currency_to == exchange_kwargs.get("currency_to")) \
            .execute()
        # print("result = " + str(result))
        if result == 0:
            exchange = ExchangeRate(**exchange_kwargs)
            exchange.save()
    except ProgrammingError:
        ExchangeRate.create_table([ExchangeRate])
        if database.table_exists("exchangerate"):
            update_record(exchange_kwargs)
        else:
            # LOGGING
            raise ProgrammingError
    except (ValueError, IntegrityError):
        pass
        # print("ERROR") LOGGING


def read_records():
    exchange_list = ExchangeRate.select()
    return list([i.__data__ for i in exchange_list])
    # for exchange in exchange_list:
    #     print(exchange.__data__)


# read_records()
# ExchangeRate.create_table([ExchangeRate])
# exchange = ExchangeRate(exchange_name="Poloniex", currency_from="USDT", currency_to="BTC", created=datetime.now(), changed=datetime.now(), buy=4001.13, sell=4007.37)
# exchange = ExchangeRate(exchange_name="Bittrex", currency_from="USD", currency_to="BTC", created=datetime.now(), changed=datetime.now(), buy=5003.33, sell=5005.55)
# exchange.save()
# users = ExchangeRate.select().where(ExchangeRate.exchange_name == "Bittrex" and ExchangeRate.buy > 5000)
# ExchangeRate.update({ExchangeRate.exchange_name: "Cryptopia"}).where(ExchangeRate.id == 3).execute()
# users = ExchangeRate.select()
#
# for u in users:
#     print(u.exchange_name)


# add_new_rate()
# some_list = [k for k in ExchangeRate.__dict__.keys() if not k.startswith("_") and not callable(getattr(ExchangeRate, k))]
# print(some_list)

# bittrex = ExchangeItem(exchange_name="Bittrex", currency_from="USD", currency_to="BTC", created=datetime.now(),
#                        changed=datetime.now(), buy=7003.33, sell=7005.55)
# print(bittrex.get_kwargs())
# update_record(bittrex.get_kwargs())

# base_list = [Poloniex(), Bitfinex(), Cryptex(), Bittrex()]
# for b in base_list:
#     result_dict = b.get_data("USD", "BTC")
#     print(result_dict)
#     update_record(result_dict)
