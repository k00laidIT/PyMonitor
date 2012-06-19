PyMonitor
=========

Sample Python scripts to show how buffer counters can be assessed programmatically on the Nexus 3000 series switches.  

What do you mean run Python on Nexus Switch?
--------------------------------------------
Nexus 3000 series switches have access to Python interpreter by default!  The possibilites are unlimited.  For an overview check out https://github.com/datacenter/Nexus/wiki/Python-on-Nexus-3000-Series-Switches---Overview

When do I use these scripts?
----------------------------

1.  Spot check buffer usage
2.  Check buffer usage while running an application to help profile network
3.  Monitor at a higher resolution then whats possible with traditional monitoring systems
4.  Integrate with existing monitoring systems to have a high resoultion view of buffer usage

How do I use the scripts?
----------------------------

Execute bufferMonitorThread.py in response to either an event or at switch startup.  This script stores per second buffer usage to a file on the bootflash.  It does not need any command line parameters.   

What else can I do with these scripts?
--------------------------------------

This script demonstrates the use of Cisco's CLI class.  Using CLI class, one could potentially monitor any counter that is accessible via the NxOS CLI.  

Alternatively, BufferDepthMonitor class which is also part of the Cisco library may also be used to monitor the buffer usage.  It provides methods to retrieve the concerned values without the awkward grep etc.,

I optimized your sample scripts - what next?
--------------------------------------------
In the spirit of sharing, please consider posting your changes back on this site.