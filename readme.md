# Crypto Homework 1 Readme

## **Author:** Todd Louison



## How to run the DES

​	This DES implementation acts as a secure chatroom, where two parties (one being a host and the other a client) can write securely to each other, and the text that is sent between the two is encrypted binary strings. This code is simple to run, requiring only two available terminals, either through a VM and Local machine, or simply two terminal instances.

1. Begin hosting the server by running the following command in one of the terminals, with*PORT NUMBER being any valid port:

   ```shell
   python3 server.py *PORT NUMBER* 
   ```

   *This server IP address is defaulted to 127.0.0.1, which is the local address of your computer. If you wish to use a different computer or virtual machine, you must change the IP address labeled "host" at the top of server.py.*

2. Now, open the client using a very similar command:

   ```
   python3 client.py
   ```

3. Once the client launches, it will ask you for the server information. Enter the IP address and port number and you will be connected!

## How the implementation works

​	For this chatroom, DES encrypts each message before being sent, and then is locally decrypted. Each time a message is sent, either from Server->Client or Client->Server, the respective party has their message converted into binary, That binary is then encrypted using the DES algorithm, and then sent to the other party as that encrypted binary. The receiving party then decrypts the message, and has their plaintext!

## How the DES is constructed

​	The DES is constructed according to the structure and permutations laid out in the 1.2 Lecture slides. I chose to break my implementation down into 3 files:

- DES.py
- desHelper.py
- SBox.py

I chose to break it down in this manner for a few reasons. Firstly the DES being a separate class allows me to initalize multiple instances of the same code, including private keys, without having to define each key variable in every file. As well, it allows the code to be much more organized than a large cluster of functions. I broke out into the separate *desHelper.py* because I realized that there were many instances where DES functions were used, but required extra work to be done with them. This was done for orderliness. The SBox class was created to be a general SBox architecture that can scale to different sized SBoxes if I decide to use larger ones for a future project.

## How the DES Works

​	First, the text given is converted to binary, then split into 8-bit chunks (padded with 0s if not a multiple of 8), and finally run through either the encryption or decryption process individually.

​	There is a 10-bit master key that is stored within the DES class, which is responsible for creating K1 and K2, which will be used later. We take our 8-bit input, and permute it. This is then split into two four bit chunks. The left chunk hangs out while we take the right chunk into our "F" function (it also gets passed to the second round).  In this function, we expand the 4-bits to 8-bits, and XOR it with K1. This value is then broken up, and used to get entries in our SBoxes by acting as row and column indexes. This value is a 2-bit number, which is then concatenated with the other SBox's output to give a new 4-bit output. This is XOR'd with the initial left key, and then sent to the next run of the "F" function. This runs identically, but replacing K1 with K2. The round happens identically to last time, and the answer is then permuted one final time to become our ciphertext!

​	This process is identical for decryption, but simply flips the order of use for K1 and K2.

## External Resources Used

​	Two external resources were used in this assignment, one to assist in the creation of the server/client socket system, and the other to convert ASCII text to binary and vice versa. The links are below

Socket Programming Tutorial:

```https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/
https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/
```

Binary converter:

```
https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
```

