# import threading
# import time
# from datetime import datetime
#

from flask import Flask
from flask import render_template
from pyenv import ENV

from course_work.additions.flask_decorator import crossdomain
#
# from course_work.exchange_parser import *
#
# CS_CURRENCIES = getattr(ENV, "CS_CURRENCIES")
# CS_UPDATE_TIME = getattr(ENV, "CS_UPDATE_TIME")
# CS_GRABBER_TIME = getattr(ENV, "CS_GRABBER_TIME")
# CS_DEBUG = getattr(ENV, "CS_DEBUG")
# CS_LOGFILE = getattr(ENV, "CS_LOGFILE")
#
#
# def exchange_grabber():
#     exchange_list = {Poloniex(), Bittrex()}
#     while True:
#         for x in exchange_list:
#             print(x.get_rate())
#         print("current_time = " + str(datetime.now()))
#         time.sleep(CS_GRABBER_TIME)
#
#
# threading.Thread(target=exchange_grabber(), args=()).start()
from course_work.database_utils import *
from course_work.grabber import *

app = Flask(__name__)
app_env = dict()
grabber = None


@app.route("/", methods=["GET"])
@crossdomain(origin='*')
def index():
    return render_template("index.html", app_env=app_env)


@app.route("/start_grabber", methods=["GET"])
@crossdomain(origin='*')
def start_grabber():
    grabber.start()
    return "Start", 200


@app.route("/stop_grabber", methods=["GET"])
@crossdomain(origin='*')
def stop_grabber():
    grabber.stop()
    return "Stop", 200


@app.route("/get_records", methods=["GET"])
@crossdomain(origin='*')
def get_records():
    return str(read_records())


if __name__ == "__main__":
    app_env = {"CS_CURRENCIES": getattr(ENV, "CS_CURRENCIES"),
               "CS_UPDATE_TIME": getattr(ENV, "CS_UPDATE_TIME"),
               "CS_GRABBER_TIME": getattr(ENV, "CS_GRABBER_TIME"),
               "CS_DEBUG": getattr(ENV, "CS_DEBUG"),
               "CS_LOGFILE": getattr(ENV, "CS_LOGFILE")}

    exchange_list = [Poloniex(), Bitfinex(), Cryptex(), Bittrex()]
    currency_list = app_env.get("CS_CURRENCIES")[1:-1].split(",")
    grabber_time = app_env.get("CS_CURRENCIES")[1:-1].split(",")
    grabber = Grabber(exchange_list, currency_list, grabber_time)

    print("exchange_list = " + str(exchange_list))
    print("currency_list = " + str(currency_list))
    print("grabber_time = " + str(grabber_time))

    # app.run(port=9000)
