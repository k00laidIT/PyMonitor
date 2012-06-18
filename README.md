PyMonitor
=========

Python scripts to monitor buffer on the Nexus 3000 series switches.

bufferMonitorThread.py
----------------------

This is the main thread that runs in a loop and collects the buffer usage stats once every second.

bufferClient.py
---------------

This script gets the requested amount of data from the main monitoring thread