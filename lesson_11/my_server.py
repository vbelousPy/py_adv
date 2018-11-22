import socket
import threading


def msg_listener(some_client, some_address):
    try:
        while True:
            data = some_client.recv(1024).decode()
            if data and not data == "q":
                with open("client_msg.txt", "a+") as f:
                    f.write("<{}> - <{}>\n".format(some_address, data))
                    f.flush()
            else:
                print("{} - connection closed".format(some_address))
                break
    except socket.timeout:
        print("{} - timeout error".format(some_address))
    some_client.close()


server_socket = socket.socket()
server_socket.bind(("", 9000))
server_socket.listen(10)
while True:
    client, address = server_socket.accept()
    client.settimeout(60)
    threading.Thread(target=msg_listener, args=(client, address)).start()
