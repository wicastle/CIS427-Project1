import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '127.0.0.1'
port = 55555
client.connect((ip, port))


def receive():
    # Server tag
    str = 'Server: '
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            str += msg
            print(str)
            str = 'Server: '
            msg = f'{input("")}'
            #print('ECHO: ' + msg)
            client.send(msg.encode('ascii'))
        except:
            print("An Error Occurred!")
            client.close()
            break


receive()


