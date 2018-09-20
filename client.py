import socket
import sys

import DES
import desHelper as DH

#Connects to the server on a given IP and Port
def connectToServer(host, port):
    mySocket = socket.socket()
    mySocket.connect((host,port))

    #Initializing my DES class, which will perform all major functions
    des = DES.toyDES()

    while True:
        inputString = input("\nEnter the message you wish to encrypt:\n -> ")

        #Exit the server if the command is 'q'
        if inputString == 'q':
            break

        #Converting inital string to binary
        inputString = DH.text_to_bits(inputString)

        #Takes the binary representation of our text, splits it into 8 bit chunks, and encrypts it
        inputList = DH.splitBinary(inputString)
        encryptedBinary = DH.runEncryption(inputList)
        message = DH.rebuildString(encryptedBinary)

        #Sends the encrypted text to the server
        mySocket.send(message.encode())

        print("Waiting for server response...")

        data = str(mySocket.recv(1024).decode())

        if data == 'q':
            print("Server has ended the session.")
            quit(1)

        print ('Encrypted text received from server: ' + data)

        #Takes the encrypted binary and turns it back to plaintext
        output = DH.text_from_bits(DH.rebuildString(DH.runDecryption(DH.splitBinary(data))))

        print ('Decrypted text: ' + output + "\n")
                
    mySocket.close()

if __name__ == '__main__':
    ip = input("Enter the IP of the server you wish to connect to\n -> ")
    port = int(input("Enter the port of the server you wish to connect to\n -> "))

    #Sends the encrypted string to the server, which will decrypt and print out the text
    connectToServer(ip, port)
