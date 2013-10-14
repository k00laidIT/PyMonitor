# The script examples provided by Cisco for your use are provided for reference only as a customer courtesay.  
# They are intended to facilitate development of your own scripts and software that interoperate with Cisco switches 
# and software.  Although Cisco has made efforts to create script examples that will be effective as aids to script 
# or software development,  Cisco assumes no liability for or support obligations related to the use of the script 
# examples or any results obtained using or referring to the script examples.

"""\n  monitorClient \n      
   \t  ... Works with monitorThread.py
   \t  ... Use:  python monitorClient.py n
   \t  ...       where n is the number of lines of data you want
   \t  ...       if n is 0 - then all the data captured so far is printed
   \t  ...       if n is -1 - then the data is copied to a file
   \t  ...       if n is -2 - then the monitorThread is stopped
   \t  ... Note: This program runs once and then ends.
   \t  ...       Developed on Python 2.7.2
   \t  ... Date: 10 July 2012 - Modified for case when no argument is given
   \t  ...       server host is the 3K chassis with the monitorThread.py running
   \t ..
   \n """

import sys                         # for parsing command line arguments
from socket import *                      # get socket constructor and constants
 
server_host = '172.25.187.8'              # server name, or IP like in this case
server_port =  50007                      # non-reserved port used by the server
message = "[b'10']"                       # text to send to server
                                          # requires bytes: b'' or str,encode()
if (len(sys.argv)) > 1:
        message = (x.encode() for x in sys.argv[1:])
        
        sockobj = socket(AF_INET, SOCK_STREAM)          # make a TCP/IP socket object
        sockobj.connect((server_host, server_port))       # connect to server machine + port

        for line in message:
                    sockobj.send(line)                  # send line to server over socket
                    data = sockobj.recv(10800)          # receive line from server

        for value in data.split(' '):
                    print (value)
                    
        sockobj.close()                                 # close socket to send eof to server
                
else:
       
       print ("Use:  python bufferClient.py  n")
       

