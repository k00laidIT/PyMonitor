#
# Name          Samuel Kommu
#

import sys
import math

def graph(aValues, min=0, maxValue=100):

        print "\n"
        counter = 0
        for value in aValues:
                line=repr(counter) + "\t " + repr(value) + "\t "
                toPrint = 0
                valRatio=int((10/float(maxValue))*float(value))
                while toPrint < valRatio:
                        line = line + "-"
                        toPrint = toPrint + 1
                print line + "*"
                counter=counter+1

values=tuple(open('/bootflash/buffer.inmem.txt','r'))

minValue=46080
maxValue=0
bufferValues=[]
for value in values:
        f, m, buffer=value.rpartition(',')
        iBuffer=int(buffer.rstrip())
#       if ( len(bufferValues) > 0 ):
#               if ( bufferValues[-1] != iBuffer ):
#                       bufferValues.append(iBuffer)
#       else:
        bufferValues.append(iBuffer)

        if minValue > iBuffer:
                minValue = iBuffer
        if maxValue < iBuffer:
                maxValue = iBuffer

print "\n"

graph(bufferValues, 0, maxValue)