import json
import os
import time
from json import JSONDecodeError
from re import match


def fix_path(fn):
    def wrapper(*args):
        dir_list = list([i for i in args])
        for i in range(len(dir_list)):
            if not dir_list[i].rfind("/") == len(dir_list[i]) - 1:
                dir_list[i] += "/"
            if not os.path.exists(dir_list[i]):
                os.makedirs(dir_list[i])
        fn(*dir_list)

    return wrapper


def execution_time(fn):
    def wrapper(number_string):
        time_start = time.time()
        result = fn(number_string)
        print(time.time() - time_start)
        return result

    return wrapper


@execution_time
def process(number_string):
    try:
        return sum(json.loads(number_string))
    except (TypeError, JSONDecodeError):
        return False


@fix_path
def monitor(read_dir, result_dir, error_dir):
    valid_files = list(filter(lambda f: os.path.isfile(read_dir + f) and match(".*\.txt$", f),
                              os.listdir(read_dir)))
    for file_name in valid_files:
        if os.path.isfile(read_dir + file_name) and match(".*\.txt$", file_name):
            fr = open(read_dir + file_name, "r")
            result = process(fr.read())
            fr.close()
            if result >= 0:
                with open(result_dir + file_name, "w") as fw:
                    fw.write(str(result))
                    os.remove(read_dir + file_name)
            else:
                if os.path.exists(error_dir + file_name):
                    os.remove(error_dir + file_name)
                os.rename(read_dir + file_name, error_dir + file_name)


while True:
    monitor("read", "result", "error")
    time.sleep(5)
