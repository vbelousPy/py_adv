import sys

arguments = sys.argv
start = int(arguments[1])
stop = int(arguments[2])
length = int(arguments[3]) + 1
result = 0
for i in range(start, stop, length):
    result += i
print("sum = " + str(result))
