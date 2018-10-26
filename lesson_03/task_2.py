import csv
import json
import pickle
import shelve
from datetime import datetime
from re import match

import xlrd as xlrd


class ValidationError(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)


class UsernameValidationError(ValidationError):
    pass


class EmailValidationError(ValidationError):
    pass


class JoinedValidationError(ValidationError):
    pass


class FileConverter:
    COLUMN_NAME = ("Username", "Email", "Joined")

    def __init__(self, file_path):
        self.user_list = list()
        error_list = list()

        xls_file = xlrd.open_workbook(file_path)
        sheet = xls_file.sheet_by_index(0)
        for row_num in range(1, sheet.nrows, 1):
            row = sheet.row_values(row_num)
            new_user = dict()
            for col_num in range(len(row)):
                new_user.update({FileConverter.COLUMN_NAME[col_num]: row[col_num]})
            try:
                self.__validate_data(new_user)
                new_user.update({FileConverter.COLUMN_NAME[2]: datetime.strftime(
                    datetime.strptime(new_user.get(FileConverter.COLUMN_NAME[2]), "%Y-%m-%d"), "%m/%d/%Y")})
                self.user_list.append(new_user)
            except ValidationError:
                error_list.append(new_user)

        if len(error_list) != 0:
            self.__error_writer(error_list)

    @staticmethod
    def __validate_data(data):
        if not match("^[A-Za-z]*$", data.get(FileConverter.COLUMN_NAME[0])):
            raise UsernameValidationError
        if not match("^[A-Za-z_.]*@[A-Za-z]*\\.[A-Za-z]*(\\.[A-Za-z]*)?$", data.get(FileConverter.COLUMN_NAME[1])):
            raise EmailValidationError
        if not match("^\\d{4}-\\d{2}-\\d{2}$", data.get(FileConverter.COLUMN_NAME[2])):
            raise JoinedValidationError

    @staticmethod
    def __error_writer(data):
        with open("errors.log", "a") as error_file:
            for s in data:
                error_file.write(str(s))

    def csv_write(self):
        with open("output.csv", "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            writer.writerow(FileConverter.COLUMN_NAME)
            for line in self.user_list:
                writer.writerow(line.values())

    def json_writer(self):
        with open("output.json", "w") as json_file:
            json.dump(self.user_list, json_file)

    def bin_writer(self):
        with open("output.bin", "wb") as bin_file:
            pickle.dump(self.user_list, bin_file)

    def shelve_writer(self):
        with shelve.open("output_shelve", "c") as shelve_file:
            for i in range(len(self.user_list)):
                shelve_file.update({str(i): self.user_list[i]})


file_converter = FileConverter("example_2.xls")
file_converter.csv_write()
file_converter.json_writer()
file_converter.bin_writer()
file_converter.shelve_writer()
