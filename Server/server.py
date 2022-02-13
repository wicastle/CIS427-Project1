import socket
import math

host = '127.0.0.1'  #local host
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

#open read and close file for logins
print('Loading logins')
lines = []
with open('logins.txt') as file_login:
    lines = file_login.readlines()
file_login.close()

rows, cols = (5, 2)
logins = [[0 for i in range(cols)] for j in range(rows)]

count = 0
for line in lines:
    count += 1
    lhs, rhs = line.split(',', 1)
    psw = rhs.replace('\n', '')
    logins[count][0] = lhs
    logins[count][1] = psw

count = 0
for login in logins:
    print(logins[count][0] + logins[count][1])
    count += 1

def file_empty(file_name):
    # Reading first character to check file is empty or not
    with open(file_name, 'r') as read_obj:
        one_char = read_obj.read(1)
        # if first character not found then file is empty
        if not one_char:
           return True
    return False


def commands(client):
    # append to end of msg
    endmsg = ' endmsg'
    newline = '\n'
    loggedin = False
    john = False
    sally = False
    qiang = False
    root = False
    shutdown = True
    while shutdown:
        try:
            msg_o = client.recv(1024).decode('ascii')
            #echo
            print('ECHO: ' + msg_o)
            msg = msg_o + endmsg
            #COMMANDS
            try:
                lhs, rhs = msg.split(' ', 1)
                if lhs == 'LOGIN':
                    user, pws, end = rhs.split(' ', 3)
                    #counter vars
                    senti = False
                    count = 0
                    #look through logins to match to user
                    for x in logins:
                        if logins[count][0] == user:
                            if logins[count][1] == pws:
                                senti = True
                                #set who is users current for file writeing
                                if user == 'root':
                                    root = True
                                else:
                                    if user == 'john':
                                        john = True
                                    else:
                                        if user == 'sally':
                                            sally = True
                                        else:
                                            if user == 'qiang':
                                                qiang = True
                                break
                            else:
                                break
                        count += 1
                    #send to client results
                    if senti:
                        client.send('SUCCESS'.encode('ascii'))
                        loggedin = True
                    else:
                        client.send('FAILURE: pls enter correct credentials'.encode('ascii'))
                else:
                    if lhs == 'SOLVE':
                        if loggedin:
                            try:
                                #write to file an ehco of what was sent
                                if root:
                                    file_root = open('root_solutions.txt', 'a')
                                    file_root.write(msg_o + newline)
                                    file_root.close()
                                else:
                                    if john:
                                        file_john = open('john_solutions.txt', 'a')
                                        file_john.write(msg_o + newline)
                                        file_john.close()
                                    else:
                                        if sally:
                                            file_sally = open('sally_solutions.txt', 'a')
                                            file_sally.write(msg_o + newline)
                                            file_sally.close()
                                        else:
                                            if qiang:
                                                file_qiang = open('qiang_solutions.txt', 'a')
                                                file_qiang.write(msg_o + newline)
                                                file_qiang.close()
                                #split rhs into -c or -r commands for solve
                                cmd, num = rhs.split(' ', 1)
                                if cmd == '-c':
                                    num1, end = num.split(' ', 1)
                                    area = math.pi * float(num1) * float(num1)
                                    area = round(area, 2)
                                    cir = 2 * math.pi * float(num1)
                                    cir = round(cir, 2)
                                    resultc = 'Circle`s circumference  is ' + str(cir) + ' and area is ' + str(area)
                                    client.send(resultc.encode('ascii'))
                                    #write solution to file
                                    if root:
                                        file_root = open('root_solutions.txt', 'a')
                                        file_root.write(resultc + newline)
                                        file_root.close()
                                    else:
                                        if john:
                                            file_john = open('john_solutions.txt', 'a')
                                            file_john.write(resultc + newline)
                                            file_john.close()
                                        else:
                                            if sally:
                                                file_sally = open('sally_solutions.txt', 'a')
                                                file_sally.write(resultc + newline)
                                                file_sally.close()
                                            else:
                                                if qiang:
                                                    file_qiang = open('qiang_solutions.txt', 'a')
                                                    file_qiang.write(resultc + newline)
                                                    file_qiang.close()
                                else:
                                    if cmd == '-r':
                                        # split once into two parts
                                        num1, end = num.split(' ', 1)
                                        #check if num2 is just the endmsg str to see if there is another number
                                        if end == 'endmsg':
                                            prim = 4 * float(num1)
                                            prim = round(prim, 2)
                                            area = float(num1) * float(num1)
                                            area = round(area, 2)
                                            resultr = 'Square`s perimeter is ' + str(prim) + ' and area is ' + str(area)
                                            client.send(resultr.encode('ascii'))
                                            # write solution to file
                                            if root:
                                                file_root = open('root_solutions.txt', 'a')
                                                file_root.write(resultr + newline)
                                                file_root.close()
                                            else:
                                                if john:
                                                    file_john = open('john_solutions.txt', 'a')
                                                    file_john.write(resultr + newline)
                                                    file_john.close()
                                                else:
                                                    if sally:
                                                        file_sally = open('sally_solutions.txt', 'a')
                                                        file_sally.write(resultr + newline)
                                                        file_sally.close()
                                                    else:
                                                        if qiang:
                                                            file_qiang = open('qiang_solutions.txt', 'a')
                                                            file_qiang.write(resultr + newline)
                                                            file_qiang.close()
                                        else:
                                            num2, x = end.split(' ', 1)
                                            prim = 2 * float(num1) + 2 * float(num2)
                                            prim = round(prim, 2)
                                            area = float(num1) * float(num2)
                                            area = round(area, 2)
                                            result = 'Rectangle`s perimeter is ' + str(prim) + ' and area is ' + str(area)
                                            client.send(result.encode('ascii'))
                                            # write solution to file
                                            if root:
                                                file_root = open('root_solutions.txt', 'a')
                                                file_root.write(result + newline)
                                                file_root.close()
                                            else:
                                                if john:
                                                    file_john = open('john_solutions.txt', 'a')
                                                    file_john.write(result + newline)
                                                    file_john.close()
                                                else:
                                                    if sally:
                                                        file_sally = open('sally_solutions.txt', 'a')
                                                        file_sally.write(result + newline)
                                                        file_sally.close()
                                                    else:
                                                        if qiang:
                                                            file_qiang = open('qiang_solutions.txt', 'a')
                                                            file_qiang.write(result + newline)
                                                            file_qiang.close()
                                    else:
                                        client.send('301 Invalid SOLVE command'.encode('ascii'))
                            except:
                                client.send('301 Error Format Type'.encode('ascii'))
                        else:
                            print('Must be logged in')
                            client.send('Must be logged in'.encode('ascii'))
                    else:
                        if lhs == 'LIST':
                            if loggedin:
                                if rhs == 'endmsg':
                                    #send back what is in file
                                    if root:
                                        fileLines = []
                                        fileReturn = ''
                                        if file_empty('root_solutions.txt'):
                                            fileReturn = '\tNo interactions yet\n'
                                        else:
                                            with open('root_solutions.txt') as file:
                                                fileLines = file.readlines()
                                            file.close()
                                            for fileLine in fileLines:
                                                fileReturn += '\t' + fileLine
                                        client.send(('root\n' + fileReturn).encode('ascii'))
                                    else:
                                        if john:
                                            fileLines = []
                                            fileReturn = ''
                                            if file_empty('john_solutions.txt'):
                                                fileReturn = '\tNo interactions yet\n'
                                            else:
                                                with open('john_solutions.txt') as file:
                                                    fileLines = file.readlines()
                                                file.close()
                                                for fileLine in fileLines:
                                                    fileReturn += '\t' + fileLine
                                            client.send(('john\n' + fileReturn).encode('ascii'))
                                        else:
                                            if sally:
                                                fileLines = []
                                                fileReturn = ''
                                                if file_empty('sally_solutions.txt'):
                                                    fileReturn = '\tNo interactions yet\n'
                                                else:
                                                    with open('sally_solutions.txt') as file:
                                                        fileLines = file.readlines()
                                                    file.close()
                                                    for fileLine in fileLines:
                                                        fileReturn += '\t' + fileLine
                                                client.send(('sally\n' + fileReturn).encode('ascii'))
                                            else:
                                                if qiang:
                                                    fileLines = []
                                                    fileReturn = ''
                                                    if file_empty('qiang_solutions.txt'):
                                                        fileReturn = '\tNo interactions yet\n'
                                                    else:
                                                        with open('qiang_solutions.txt') as file:
                                                            fileLines = file.readlines()
                                                        file.close()
                                                        for fileLine in fileLines:
                                                            fileReturn += '\t' + fileLine
                                                    client.send(('qiang\n' + fileReturn).encode('ascii'))
                                else:
                                    flag, end = rhs.split(' ', 1)
                                    if flag == '-all':
                                        if root:
                                            totalReturn = ''
                                            fileLines_root = []
                                            fileReturn_root = ''
                                            if file_empty('root_solutions.txt'):
                                                fileReturn_root = '\tNo interactions yet\n'
                                            else:
                                                with open('root_solutions.txt') as file_root:
                                                    fileLines_root = file_root.readlines()
                                                file_root.close()
                                                for fileLine_root in fileLines_root:
                                                    fileReturn_root += '\t' + fileLine_root
                                            totalReturn += 'root\n' + fileReturn_root

                                            fileLines_john = []
                                            fileReturn_john = ''
                                            if file_empty('john_solutions.txt'):
                                                fileReturn_john = '\tNo interactions yet\n'
                                            else:
                                                with open('john_solutions.txt') as file_john:
                                                    fileLines_john = file_john.readlines()
                                                file_john.close()
                                                for fileLine_john in fileLines_john:
                                                    fileReturn_john += '\t' + fileLine_john
                                            totalReturn += 'john\n' + fileReturn_john

                                            fileLines_sally = []
                                            fileReturn_sally = ''
                                            if file_empty('sally_solutions.txt'):
                                                fileReturn_sally = '\tNo interactions yet\n'
                                            else:
                                                with open('sally_solutions.txt') as file_sally:
                                                    fileLines_sally = file_sally.readlines()
                                                file_sally.close()
                                                for fileLine_sally in fileLines_sally:
                                                    fileReturn_sally += '\t' + fileLine_sally
                                            totalReturn += 'sally\n' + fileReturn_sally

                                            fileLines_qiang = []
                                            fileReturn_qiang = ''
                                            if file_empty('qiang_solutions.txt'):
                                                fileReturn_qiang = '\tNo interactions yet\n'
                                            else:
                                                with open('qiang_solutions.txt') as file_qiang:
                                                    fileLines_qiang = file_qiang.readlines()
                                                file_qiang.close()
                                                for fileLine_qiang in fileLines_qiang:
                                                    fileReturn_qiang += '\t' + fileLine_qiang
                                            totalReturn += 'qiang\n' + fileReturn_qiang
                                            client.send(totalReturn.encode('ascii'))

                                        else:
                                            client.send('ERROR: Must be root user'.encode('ascii'))
                                    else:
                                        client.send('301 Invalid LIST command'.encode('ascii'))
                            else:
                                print('Must be logged in')
                                client.send('Must be logged in'.encode('ascii'))
                        else:
                            if lhs == 'LOGOUT':
                                if loggedin:
                                    print('logout')
                                    loggedin = False
                                    root = False
                                    client.send('200 OK'.encode('ascii'))
                                else:
                                    print('Must be logged in')
                                    client.send('Must be logged in'.encode('ascii'))
                            else:
                                if lhs == 'SHUTDOWN':
                                    if root:
                                        print('shutdown')
                                        client.send('200 OK'.encode('ascii'))
                                        shutdown = False
                                        return False
                                    else:
                                        print('Must be root')
                                        client.send('Must be root'.encode('ascii'))
                                else:
                                    print('300 Invalid Command')
                                    client.send('300 Invalid Command'.encode('ascii'))
            except:
                print('!CIRTICAL ERROR!')
                client.send('ERROR has occured'.encode('ascii'))
        except:
            client.close()
            return True


def receive():
    shutdown = True
    while shutdown:
        client, address = server.accept()
        print(f'connected with {str(address)}')
        client.send('Connected to the Server!'.encode('ascii'))
        shutdown = commands(client)


print("Starting Server . . .")
#main scpirt
receive()
print("Shutting Down Server . . .")