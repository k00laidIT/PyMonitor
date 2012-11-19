# The script examples provided by Cisco for your use are provided for reference only as a customer courtesay.  
# They are intended to facilitate development of your own scripts and software that interoperate with Cisco switches 
# and software.  Although Cisco has made efforts to create script examples that will be effective as aids to script 
# or software development,  Cisco assumes no liability for or support obligations related to the use of the script 
# examples or any results obtained using or referring to the script examples.

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
\t ... Date 10 Jul 2012 - Added: autodetect for server_host IP address
\t ..
\n """

from cisco import *            # Cisco library - for CLI etc.,
from datetime import datetime  # for timestamp
from time import sleep         # sleep
from sys import *              # for parsing command line arguments 
from socket import *           # get socket constructor and constants
from string import join        # forthe response

#  server_host = '172.25.187.8'   # server name, or IP like in this case
server_port = 50007            # listen on a non-reserved port number

# Get server IP

s, inf1 = cli("show int mgmt0 brief | grep mgmt0");  o = inf1       
o = o.replace ("mgmt0",""); o = o.replace ("--",""); o = o.replace ("up",""); inf = o.lstrip()

myHost = inf.split(" ")[0]                  # server name, or IP

#............ End of serverHost section




# File where the buffer values will be stored - if requested
buffer_file_name = "/bootflash/buffer_usage.log"

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
    if (connection_failed != True):             # If there were new connections ---
        data = int(connection.recv(10800))        # read next line on client socket
        bv_count = len(buffer_values)               # the # of values we have in memory
        if (data < bv_count):                   # Check that request is within range
            if (data == -2):      # Done with the monitoring - close the main thread
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
