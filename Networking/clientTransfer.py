import socket
import time

def Main(protocol):
    Host = socket.gethostname()#'127.0.0.1'
    Port = 5001 #65002
    if protocol.lower() == "t":
        Soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP

        Soc.connect((Host,Port))
        Soc.send(b'50')
        cont = Soc.recv(1024)
        file = open("NewFile.png", 'wb')
        starting = time.time()
        while True:
            fileData = Soc.recv(1024)
            if not fileData:
                break
            file.write(fileData)
        ending = time.time()
        file.close()
        print(ending - starting,"time to send file")
        Soc.close()

    else:
        Soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #UDP

        Soc.sendto(b'50', (Host, Port))
        file = open("NewFile.png", 'wb')
        starting = time.time()
        while True:
            fileData, address = Soc.recvfrom(1024)
            if fileData == b'end':
                break
            file.write(fileData)
        ending = time.time()
        file.close()
        print(ending - starting,"time to send file")
        Soc.close()

if __name__ == '__main__':
    Main("T")
    #Main("U")
