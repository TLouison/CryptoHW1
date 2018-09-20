import sys
import socket

import desHelper as DH
import time
 
def Main(port):
    host = "127.0.0.1"
    
    #Links the socket to the ip and port to allow connection to it
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    print("Waiting for connection...")
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()

            #Conditionals to decide when to kill the server
            if not data:
                break
            if data == 'q':
                print("Client has ended the session.")
                break

            print ("Encrypted text received: " + str(data))

            #Decrypts the encrypted text from the user
            encryptedList = DH.splitBinary(data)
            decryptedBinary = DH.runDecryption(encryptedList)
            output = DH.rebuildString(decryptedBinary)
            output = DH.text_from_bits(output)

            print("Decrypted text: " + output + "\n")
        
            #Now it is the server's turn to send an encrypted message to the user!
            inputString = input("Enter the message you wish to encrypt:\n -> ")

            #If the server wants to quit, type q to break the loop
            if inputString == "q":
                conn.send('q'.encode())
                break
            else:
                #Converting inital string to binary
                inputString = DH.text_to_bits(inputString)

                #Takes the binary representation of our text, splits it into 8 bit chunks, and encrypts it
                inputList = DH.splitBinary(inputString)
                encryptedBinary = DH.runEncryption(inputList)
                message = DH.rebuildString(encryptedBinary)

                #Sends the encrypted text back to the user
                conn.send(message.encode())
                
    conn.close()

if __name__ == '__main__':
    Main(int(sys.argv[1]))