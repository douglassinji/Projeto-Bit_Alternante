from socket import *
from time import sleep


# Function for reply the sender msg
def ack_resp():
    if message[0] == "0":
        server_socket.sendto("ACK0".encode(), client_address)
        print("SENT: ACK0")
        print("")
    elif message[0] == "1":
        server_socket.sendto("ACK1".encode(), client_address)
        print("SENT: ACK1")
        print("")


# Function to avoid user type error
def port_req():
    # Requesting port number
    port = input("Please select a port number from 10001 to 11000: ")
    # Checking if the port# is valid
    while True:
        try:
            port = int(port)
            if not 10001 <= port <= 11000:
                print("")
                port = input("Invalid Number!! Please enter a integer number from 10001 to 11000:   ")
                continue
            else:
                print(f'PORT NUMBER {port} ACCEPTED!')
                print("")
                break
        except:
            print("")
            port = input("Invalid Number!! Please enter a integer number from 10001 to 11000:   ")
            continue

    return port


server_port = port_req()
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
counter = 1

print("Waiting for a message... ")
print("")

while True:
    global len_qtd_msg
    package, client_address = server_socket.recvfrom(2048)
    message = package.decode()
    print("RECV: " + message)

    if counter == 1:
        len_qtd_msg = len(message) - 2
        counter += 1

    if len_qtd_msg == 1:
        if message[1] == message[2]:
            ack_resp()
            server_socket.close()
            print("")
            print("Connection closed")
            break

    if len(message) == 2*len_qtd_msg +1:
        if message[1:len_qtd_msg+1] == message[(len_qtd_msg + 1):(len_qtd_msg * 2+1)]:
            ack_resp()
            server_socket.close()
            print("")
            print("Connection closed")
            break

    ack_resp()
