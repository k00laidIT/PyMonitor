#
# Name                  Samuel Kommu
# Modified from         Jacob Rapp's SocketClient.py
# Modified              To run on more versions of Python by R. Stellman
#                       And added help section

"""\n  bufferClient \n      
   \t  ... Works with bufferMonitorThread.py
   \t  ... Use:  python bufferClient.py  n
   \t  ...       where n is the number of lines of data you want
   \t  ... Note: This program runs once and then ends.
   \t  ...       Developed on Python 2.7.2
   \t ..
   \n """

import sys
from cisco import *
from socket import *                            # get socket constructor and constants
serverHost = '10.10.1.201'                      # server name, or IP like in this case
serverPort =  50007                             # non-reserved port used by the server

message = "[b'10']"                             # default text to send to server
                                                # requires bytes: b'' or str,encode()
if len(sys.argv) > 1:
        message = (x.encode() for x in sys.argv[1:])

sockobj = socket(AF_INET, SOCK_STREAM)          # make a TCP/IP socket object
sockobj.connect((serverHost, serverPort))       # connect to server machine + port

for line in message:
        sockobj.send(line)                      # send line to server over socket
        data = sockobj.recv(10800)              # receive line from server
        for value in data.split(' '):
                print (value)

sockobj.close()                                # close socket to send eof to server
