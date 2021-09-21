# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, Server')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import socket
import dns.resolver

run = True
while run:
    quer = input('Do you want to throw a query:' )
# A
    result = dns.resolver.resolve('sync.deakin.edu.au', 'A')
    for IPvalue in result:
        print('IP', IPvalue.to_text())
# CNAME
    result1 = dns.resolver.resolve('sync.deakin.edu.au', 'CNAME')
    for Cname in result1:
        print('Cname target address:', Cname.target)

# Query-Response
    my_name = socket.gethostname(  )
    my_addr = socket.gethostbyname(my_name)
    the_name, aliases, addresses = socket.gethostbyaddr(my_addr)
    print('Primary name for %s (%s): %s' % (my_name, my_addr, the_name))
    for alias in aliases: print("AKA", alias)
    for address in addresses: print("address:", address)

    import requests

    response = requests.get('https://google.com')
    print(response.status_code)
    if response.status_code == 200:
      print('Success!')
    elif response.status_code == 404:
        print('Not Found.')

    from socket import *

    serverName = "127.0.0.1"
    serverPort = 11500
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = "Hello SIT202"
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    ServerReply, serverAddress = clientSocket.recvfrom(2048)
    print('Server reply:',
          ServerReply.decode())  # bytes = b'...' literals = a sequence of octets (integers between 0 and 255)

    if quer == "n":
        run = False
        clientSocket.close()
