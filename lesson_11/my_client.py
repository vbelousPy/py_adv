import socket


client_socket = socket.socket()
client_socket.connect(("localhost", 9000))
try:
    some_text = ""
    while not some_text == "q":
        some_text = input("Enter msg: ")
        client_socket.send(str.encode(some_text))
    client_socket.close()
except ConnectionAbortedError:
    print("Connection broken...")
