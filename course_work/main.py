import threading

from flask import Flask
from flask import jsonify
from flask import render_template
from pyenv import ENV

from course_work.additions.flask_decorator import crossdomain
from course_work.database_utils import *
from course_work.grabber import *

app = Flask(__name__)
app_env = dict()
grabber = None


@app.route("/", methods=["GET"])
@crossdomain(origin='*')
def index():
    logging.debug(str(datetime.now()) + " index")
    return render_template("index.html", app_env=app_env)


@app.route("/start_grabber", methods=["GET"])
@crossdomain(origin='*')
def start_grabber():
    logging.debug(str(datetime.now()) + " start_grabber")
    threading.Thread(target=grabber.start(), args=()).start()
    return "Start", 200


@app.route("/stop_grabber", methods=["GET"])
@crossdomain(origin='*')
def stop_grabber():
    logging.debug(str(datetime.now()) + " stop_grabber")
    grabber.stop()
    return "Stop", 200


@app.route("/get_records", methods=["GET"])
@crossdomain(origin='*')
def get_records():
    logging.debug(str(datetime.now()) + " get_records")
    return jsonify(read_records())


if __name__ == "__main__":
    app_env = {"CS_CURRENCIES": getattr(ENV, "CS_CURRENCIES"),
               "CS_UPDATE_TIME": getattr(ENV, "CS_UPDATE_TIME"),
               "CS_GRABBER_TIME": getattr(ENV, "CS_GRABBER_TIME"),
               "CS_DEBUG": getattr(ENV, "CS_DEBUG"),
               "CS_LOGFILE": getattr(ENV, "CS_LOGFILE")}

    logging_level = logging.INFO if app_env.get("CS_DEBUG") else logging.ERROR
    logging.basicConfig(filename=app_env.get("CS_LOGFILE"), level=logging_level)
    logging.debug(str(datetime.now()) + " app_env = " + str(app_env))

    exchange_list = [Poloniex(), Bitfinex(), Cryptex(), Bittrex()]
    currency_list = app_env.get("CS_CURRENCIES")[1:-1].split(",")
    grabber_time = app_env.get("CS_GRABBER_TIME")
    grabber = Grabber(exchange_list, currency_list, grabber_time)

    app.run(port=9000)
