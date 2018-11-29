from random import random
import subprocess
import time


def get_random_str(max):
    return str(int(random() * max))


for i in range(3):
    p = subprocess.Popen("python slave.py {} {} {}".format(get_random_str(10), get_random_str(100), get_random_str(10)),
                         shell=True)
    p.wait()
    print("pid =", p.pid)
    time.sleep(0.5)
