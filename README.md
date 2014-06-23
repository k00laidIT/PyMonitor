PyMonitor
=========

Sample Python scripts to show how any counters can be assessed programmatically on the Nexus series switches.  For this example we use the Max Cell Usage counter under buffer counters.  

What do you mean run Python on Nexus Switch?
--------------------------------------------
Nexus series switches, starting with 3000 series, have access to Python interpreter by default!  The possibilites are unlimited.  For all the nitty-gritty details check out  http://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus3000/sw/python/api/python_api/API_functions.html

When do I use these scripts?
----------------------------

1.  Spot check buffer usage
2.  Check buffer usage while running an application to help profile network
3.  Monitor at a higher resolution then whats possible with traditional monitoring systems
4.  Integrate with existing monitoring systems to have a high resoultion view of buffer usage

How do I use the scripts?
----------------------------

Execute monitorThread.py in response to either an event or at switch startup.  This script stores per second buffer usage.  It does not need any command line parameters.  This script also implements sockets using which one could send messages to the Thread.  monitorClient.py is an example script to send messages to the monitorThread.py.  Using monitorClient.py, one could send a message to monitorThread.py to 1. save the values to disk, 2. send all or subset of values.  Script monitorClient.py does not need to run on the switch - it could run on any server!  Note:  care should be taken to avoid security compromise.  To get details on how to run Python scripts on Nexus check out http://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus3000/sw/python/api/python_api/API_functions.html 

What else can I do with these scripts?
--------------------------------------

This script demonstrates the use of Cisco's CLI class.  Using CLI class, one could potentially monitor any counter that is accessible via the NxOS CLI.  

Alternatively, BufferDepthMonitor class which is also part of the Cisco library may also be used to monitor the buffer usage.  It provides methods to retrieve the concerned values without the awkward grep etc.,

I optimized your sample scripts - what next?
--------------------------------------------
In the spirit of sharing, please consider posting your changes back on this site.

These scripts were tested on
----------------------------
Nexus 3000 - Runnning Cisco NX-OS Release 5.0(3)U3(1) and above
<br>Nexus 5000 - <i>Coming Soon....</i>
<br>Nexus 7000 - <i>Coming Soon....</i>
