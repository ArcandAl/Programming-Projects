import socket

def Main(option):
    host = socket.gethostname()  #"127.0.0.1"
    port = 5001 #65002

    if option == "TCP":
        tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
        tcpSocket.bind((host, port))
    else:
        udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # UDP
        udpSocket.bind((host, port))

    if option == "TCP":
        tcpSocket.listen(1)  # number of unaccepted connections system will allow before refusing new connections
        newSocket, address = tcpSocket.accept()  # returns new socket object and address bound to the socket
        data = newSocket.recv(1024)

        if data == b'2':
            filename = 'test2MB.png'
            print("2 MB file selected")
        elif data == b'10':
            filename = "test10MB.png"
            print("10 MB file selected")
        elif data == b'20':
            filename = "test20MB.png"
            print("20 MB file selected")
        elif data == b'50':
            filename = "test50MB.png"
            print("50 MB file selected")
        elif data == b'100':
            filename = "test100MB.png"
            print("100 MB file selected")
        elif data == b'200':
            filename = "test200MB.png"
            print("200 MB file selected")
        else:
            print("No file selected")

        while True:

            file = open(filename, 'rb')  # open file to read in binary mode
            content = file.read(1024)
            while content:
                newSocket.send(content)
                content = file.read(1024)
            file.close()
            print("File sent")
            newSocket.close()
            break
        tcpSocket.close()

    else:
        data, address = udpSocket.recvfrom(1024)

        if data == b'2':
            filename = 'test2MB.png'
            print("2 MB file selected")
        elif data == b'10':
            filename = "test10MB.png"
            print("10 MB file selected")
        elif data == b'20':
            filename = "test20MB.png"
            print("20 MB file selected")
        elif data == b'50':
            filename = "test50MB.png"
            print("50 MB file selected")
        elif data == b'100':
            filename = "test100MB.png"
            print("100 MB file selected")
        elif data == b'200':
            filename = "test200MB.png"
            print("200 MB file selected")
        else:
            print("No file selected")


        file = open(filename, 'rb')  # open file to read in binary mode
        content = file.read(1024)
        while content:
            udpSocket.sendto(content, address)
            content = file.read(1024)
        file.close()
        message = "end"
        udpSocket.sendto(message.encode(), address)
        print("File sent")
        udpSocket.close()


if __name__ == '__main__':
    Main("TCP")
    #Main("UDP")
