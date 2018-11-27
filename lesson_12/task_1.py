from flask import Flask, request
import csv

app = Flask(__name__)


@app.route("/list", methods=["GET"])
def get_list():
    try:
        return str(csv_read(request.args.get("name"))), 200
    except (EOFError, FileExistsError, FileNotFoundError, IOError):
        return "Error", 404


@app.route("/add", methods=["POST"])
def add_data():
    try:
        request_data = request.form
        if len(csv_read(name=request_data.get("product_name"))) == 0:
            with open("data.csv", "a+") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([request_data.get("product_name"), request_data.get("amount")])
                return "Ok", 200
        else:
            return "Already exists", 400
    except (EOFError, FileExistsError, FileNotFoundError, IOError):
        return "Error", 404


def csv_read(name=None):
    try:
        with open("data.csv", "r+") as csv_file:
            csv_reader = csv.reader(csv_file)
            returned_list = list()
            for row in csv_reader:
                if name is None or name == row[0]:
                    returned_list.append({"product_name": row[0], "amount": row[1]})
        return returned_list
    except FileNotFoundError:
        return list()


if __name__ == "__main__":
    app.run(port=9000)
