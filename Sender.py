from socket import *    # Import socket module
import platform         # For getting the operating system name
import subprocess       # For executing a shell command

global port_num
global receiver_ip
global msgs
global data
global packages

seqno = "0"
ack = "ACK1"

# Ping function copied from  -->>>   https://stackoverflow.com/questions/2953462/pinging-servers-in-python
# It will return True if host responding or false if it is not responding
def ping(ip_addr):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', ip_addr]

    return subprocess.call(command) == 0


# Function to ask user the port number and avoid user type error
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


# Function to ask user the ip address from the receiver and avoid user type error
def receiver_ip_req():
    # Requesting the IP address
    ip = input("Please enter receiver IP: ")
    # Checking if host address is "pinging"
    while True:
        if ping(ip):
            print("")
            print("")
            print(f"{ip.upper()} IS RESPONDING. PING STATUS = OK!!!")
            print("")
            break
        else:
            print("")
            print(f"{ip} IS NOT RESPONDING. PLEASE CHECK THE ADDRESS AND TRY AGAIN!")
            ip = input("ENTER THE RECEIVER IP: ")
            print("")
    return ip


# Function to ask user the qty of msgs that will be sent and avoid user type error
def msgs():
    qtd_msgs = input("How many msgs do you want to send: ")
    while True:
        try:
            qtd_msgs = int(qtd_msgs)
            print("")
            break
        except:
            qtd_msgs = input("INVALID VALUE! PLEASE ENTER A INTEGER NUMBER: ")
            print("")

    return qtd_msgs


# Function to Building dictionary with packages that will be sent
def packages():
    data_ = []

    for p in range(1, msgs + 1):
        package_ = str(p) + str(msgs)
        data_.append(package_)
    return data_


counter = 0
msgs = msgs()
packages = packages()
client_socket = socket(AF_INET, SOCK_DGRAM)
server_port = port_req()
receiver_ip = receiver_ip_req()
print("")

for p in packages:

    client_socket.settimeout(1)
    new_package = seqno + p

    while seqno != ack[3]:
        try:
            client_socket.sendto(new_package.encode(), (receiver_ip, server_port))
            print("SENT: " + new_package)
            response, server_address = client_socket.recvfrom(2048)
            response = response.decode()
            ack = response
        except:
            pass

    # If ack is received, seqno will be change to send a new msg
    if ack == "ACK0":
        seqno = "1"
        counter += 1
        pass
    elif ack == "ACK1":
        seqno = "0"
        counter += 1
        pass

    print("RECV: " + response)
    print("")

    # Will close the socket after receive all the msgs
    if counter > msgs:
        print("b")
        print("Connection_Closed")
        client_socket.close()
        break
