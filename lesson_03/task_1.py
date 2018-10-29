import os
import sys


def revers_file(file_path):
    with open(file_path, "rb+") as f:
        f_len = 0
        while f.read(1):
            f_len += 1
        for i in range(f_len):
            for j in range(f_len - i - 1):
                f.seek(j)
                current_symbols = f.read(2)
                f.seek(j)
                f.write(current_symbols[::-1])
                j += 1


file_name = sys.argv[1]
if os.path.exists(file_name):
    revers_file(file_name)
else:
    print("file not found")
