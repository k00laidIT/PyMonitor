#
#                            Cisco-Style BSD
#                 Copyright (c) 2012, Cisco Systems, Inc
#                          All rights reserved.
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer. 
#
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation 
# and/or other materials provided with the distribution. 
#
# * Neither the name of Cisco, the name of the copyright holder nor the names
# of their respective contributors may be used to endorse or promote products
# derived from this software without specific prior written permission. 
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
"""\n  monitorClient \n      
   \t  ... Works with monitorThread.py
   \t  ... Use:  python monitorClient.py n
   \t  ...       where n is the number of lines of data you want
   \t  ...       if n is 0 - then all the data captured so far is printed
   \t  ...       if n is -1 - then the data is copied to a file
   \t  ...       if n is -2 - then the monitorThread is stopped
   \t  ... Note: This program runs once and then ends.
   \t  ...       Developed on Python 2.7.2
   \t ..
   \n """

from sys import *                         # for parsing command line arguments
from socket import *                      # get socket constructor and constants
 
server_host = '172.25.187.8'              # server name, or IP like in this case
server_port =  50007                      # non-reserved port used by the server
message = "[b'10']"                       # text to send to server
                                          # requires bytes: b'' or str,encode()
if len(argv) > 1:
    message = (x.encode() for x in argv[1:])

sock_obj = socket(AF_INET, SOCK_STREAM)       # make a TCP/IP socket object
sock_obj.connect((server_host, server_port))  # connect to server machine + port

for line in message:
    sock_obj.send(line)                   # send line to server over socket
    data = sock_obj.recv(10800)           # receive lines from server
    for value in data.split(' '):         # split at [SPACE] into lines 
        print (value)                     # print each of those lines

sock_obj.close()                          # close socket to send eof to server

