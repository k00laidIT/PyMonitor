PyMonitor
=========

Sample Python scripts to show how any counters can be assessed programmatically on the Nexus series switches.  For this example we use the Max Cell Usage counter under buffer counters.  

What do you mean run Python on Nexus Switch?
--------------------------------------------
Nexus series switches, starting with 3000 series, have access to Python interpreter by default!  The possibilites are unlimited.  For all the nitty-gritty details check out https://github.com/datacenter/Nexus/wiki/Python-on-Nexus-3000-Series-Switches

When do I use these scripts?
----------------------------

1.  Spot check buffer usage
2.  Check buffer usage while running an application to help profile network
3.  Monitor at a higher resolution then whats possible with traditional monitoring systems
4.  Integrate with existing monitoring systems to have a high resoultion view of buffer usage

How do I use the scripts?
----------------------------

Execute monitorThread.py in response to either an event or at switch startup.  This script stores per second buffer usage to a file on the bootflash.  It does not need any command line parameters.  To get details on how to run Python scripts on Nexus check out https://github.com/datacenter/Nexus/wiki/Python-on-Nexus-3000-Series-Switches 

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