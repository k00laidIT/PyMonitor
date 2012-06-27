#
#                            Cisco-Style BSD
#                 Copyright (c) 2010, Cisco Systems, Inc
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
"""\n monitorThread \n
\t ... Works with monitorClient.py
\t ... Use: python monitorThread
\t ... Input:  number of lines to output;  
\t             -2 to close thread
\t             -1 to write to file
\t              0 to send out all values
\t
\t ... Note: This program runs continously until you disconnect
\t ... Developed on Python 2.7.2
\t ..
\n """

from cisco import *            # Cisco library - for CLI etc.,
from datetime import datetime  # for timestamp
from time import sleep         # sleep
from sys import *              # for parsing command line arguments 
from socket import *           # get socket constructor and constants
from string import join        # forthe response

server_host = '172.25.187.8'   # server name, or IP like in this case
server_port = 50007            # listen on a non-reserved port number
# File where the buffer values will be stored - if requested
buffer_file_name = "/bootflash/buffer.inmem.txt"

sock_obj = socket(AF_INET, SOCK_STREAM)    # make a TCP socket object
sock_obj.bind((server_host, server_port))  # bind it to server:port number
sock_obj.listen(5)                         # listen, allow 5 pending connects
sock_obj.setblocking(0)                    # return immediately if no pending connects

buffer_values = []                         # store buffer values in memory 

# using Cisco's CLI class to get the buffer usage stats
cli_obj = CLI('show hardware internal buffer info pkt-stats brief', False)

while True:                                # listen until process is killed/stopped
    connection_failed = False              # assume the connection has failed :/
    cur_date=datetime.now().strftime("%y/%m/%d,%H:%M:%S")   # for timestamp
    cli_obj.rerun()                        # run the buffer cli command
    # from raw output, get the 4th line after splitting on new line "\n"
    f, m, buffer_usage = cli_obj.get_raw_output().split("\n")[4].rpartition(' ')
    # add the values to the buffer_values list
    buffer_values.append(cur_date + "," + buffer_usage)
    sleep(1)                               # sleep for a second
    try:
        connection, address = sock_obj.accept()   # Check for any connection requests
    except :                                      # may fail if no new connections
        connection_failed = True                  # so, if no connection requests 
        pass                                      # dont break - just continue
    if ( connection_failed != True ):             # If there were new connections ---
        data = int(connection.recv(10800))        # read next line on client socket
        bv_count=len(buffer_values)               # the # of values we have in memory
        if ( data < bv_count ):                   # Check that request is within range
            if ( data == -2 ):      # Done with the monitoring - close the main thread
                break;
            if ( data == -1 ):                             # Save to file ...
                buffer_file = open(buffer_file_name, 'w')  # open file in write mode
                for value in buffer_values:                # for each value in memory
                    buffer_file.write("%s\n" % value)      # print it to file
                    buffer_file.close()                    # save and close
            elif ( data == 0 ):                            # Send out all the values 
                connection.send(join(buffer_values))
            else:                         # Send out a range of values - last x units
                connection.send(join(buffer_values[(bv_count-data):bv_count]))
        else:                                       # don't the # of values asked for
                connection.send("Invalid index")
        connection.close()
