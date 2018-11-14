import os
from re import match


class LogReader:

    def __init__(self, path=".\\", mask="*.log") -> None:
        if not path.rfind("/") == len(path) - 1:
            path += "/"
        self.path = path
        self.mask = ".*\\" + mask[1:] + "$"

        self.valid_files = list(
            filter(lambda l: os.path.isfile(self.path + l) and match(self.mask, l), os.listdir(self.path)))

        self.log_list = list()
        for next_file in self.valid_files:
            with open(self.path + next_file, "r") as f:
                self.log_list.extend([fl[:-1] for fl in f.readlines()])

    def __iter__(self):
        return iter(self.log_list)

    @property
    def files(self):
        return [f for f in self.valid_files]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with LogReader(path="./some_folder/", mask="*.log") as log_reader:
    print(log_reader.files)
    for i in log_reader:
        print(i)
