import logging
from datetime import datetime

from peewee import *

database = MySQLDatabase("local_database", user='root', password='somepassword', host='127.0.0.1', port=3306)


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
        result = ExchangeRate \
            .update({ExchangeRate.changed: exchange_kwargs.get("changed"), ExchangeRate.buy: exchange_kwargs.get("buy"),
                     ExchangeRate.sell: exchange_kwargs.get("sell")}) \
            .where(ExchangeRate.exchange_name == exchange_kwargs.get("exchange_name"),
                   ExchangeRate.currency_from == exchange_kwargs.get("currency_from"),
                   ExchangeRate.currency_to == exchange_kwargs.get("currency_to")) \
            .execute()
        if result == 0:
            exchange = ExchangeRate(**exchange_kwargs)
            exchange.save()
    except ProgrammingError:
        ExchangeRate.create_table([ExchangeRate])
        if database.table_exists("exchangerate"):
            update_record(exchange_kwargs)
        else:
            logging.error(str(datetime.now()) + " table not found")
            raise ProgrammingError
    except (ValueError, IntegrityError):
        logging.error(str(datetime.now()) + " parsing error " + exchange_kwargs.get("exchange_name"))


def read_records():
    try:
        return list([i.__data__ for i in ExchangeRate.select()])
    except ProgrammingError:
        return []
