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

# Help
"""\n bufferMonitorThread \n
\t ... Works with bufferClient.py
\t ... Use: python bufferMonitorThread
\t ... Input:  number of lines to output;  
\t             -2 to close thread
\t             -1 to write to file
\t              0 to send out all values
\t
\t ... Note: This program runs continously until you disconnect
\t ... Developed on Python 2.7.2
\t ..
\n """


# imports, includes etc
from cisco import *
from datetime import datetime
import time
from socket import *
from sys import *
from string import join

myHost = ''                                                     # '' = all available interfaces on host
myPort = 50007                                                  # listen on a non-reserved port number

sockobj = socket(AF_INET, SOCK_STREAM)                          # make a TCP socket object
sockobj.bind((myHost, myPort))                                  # bind it to server port number
sockobj.listen(3)                                               # listen, allow 3 pending connects
sockobj.settimeout(1)                                           # Timeout if it takes more then a second 

bufferValues = []
oCli = CLI('show hardware internal buffer info pkt-stats brief', False)

counter=0
while True:                                                     # listen until process killed
        connectionFailed = False
        curDate=datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        oCli.rerun()
        f, m, bUsage = oCli.get_raw_output().split("\n")[4].rpartition(' ')
        bufferValues.append(curDate + "," + bUsage)
        #time.sleep(1)
        
        try:
                connection, address = sockobj.accept()          # Check for any connection requests
        except timeout, msg:    
                connectionFailed = True                         # In case of no connection requests - 
                pass
        if ( connectionFailed != True ):
                data = int(connection.recv(10800))            # read next line on client socket
                bvCount=len(bufferValues)
                # Check that request is within range
                if ( data < bvCount ):
                        # Done with the monitoring - close the main thread
                        if ( data == -2 ):
                                break;
                        # Save to file ...
                        if ( data == -1 ):
                                bufferFileName = "/bootflash/buffer.inmem.txt"
                                bufferFile = open(bufferFileName, 'w')
                                for Value in bufferValues:
                                        bufferFile.write("%s\n" % Value)
                                bufferFile.close()
                        # Send out all the values
                        elif ( data == 0 ):
                                connection.send(join(bufferValues))
                        # Send out a range of values - last x units
                        else:
                                connection.send(join(bufferValues[(bvCount-data):bvCount]))
                else:
                        connection.send("Invalid index")
                connection.close()
