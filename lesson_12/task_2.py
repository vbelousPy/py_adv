from re import *

reg_host = "\w*[a-z.A-Z]+\w*"
reg_ip = "(?:(?:[0-1]?\d{,2}|2[0-4]\d|25[0-5])\." \
         "(?:[0-1]?\d{,2}|2[0-4]\d|25[0-5])\." \
         "(?:[0-1]?\d{,2}|2[0-4]\d|25[0-5])\." \
         "(?:[0-1]?\d{,2}|2[0-4]\d|25[0-4]))"
reg_port = "[1-9]\d{,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d{1}|6553[0-5]"
regular = "^(" + reg_host + "|" + reg_ip + "):(" + reg_port + ")$"
string_list = ["localhost:5000", "127.0.0.1:65535", "255.255.255.255:8080"]
try :
    for string in string_list:
        result = match(regular, string)
        print(result.groups())
except AttributeError:
    print("Error")

