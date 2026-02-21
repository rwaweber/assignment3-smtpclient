import socket

debug = False

def smtp_command(command, commandSocket):
    formatted_command = f"{command}\r\n"
    commandSocket.send(formatted_command.encode())
    recv = commandSocket.recv(1024).decode()
    if debug:
        print(f"Received after {command}: {recv}")
        if recv[:3] == '354':
            print("354, starting data write")
        elif recv[:3] == '221':
            print("221, client disconnecting")
        elif recv[:3] != '250':
            print('250 reply not received from server.')


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message\r\n"
    endmsg = "\r\n."

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    if debug:
        print(f"Received after connect {recv}") #You can use these print statement to validate return codes from the server.
        if recv[:3] != '220':
            print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if debug:
        print(f"Received after helo: {recv1}")
        if recv1[:3] != '250':
            print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    smtp_command("MAIL FROM: <rww8018@nyu.edu>", clientSocket)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    smtp_command("RCPT TO: <rwaweber@gmail.com>", clientSocket)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    smtp_command("DATA", clientSocket)
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    #smtp_command(msg, clientSocket)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    smtp_command(endmsg, clientSocket)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    smtp_command("QUIT", clientSocket)
    # Fill in end

    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
