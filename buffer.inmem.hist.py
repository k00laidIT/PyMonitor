#
# Name          Samuel Kommu
#

import sys
import math

def hist(aValues, bins=5, min=0, max=100):
        range=(max-min)/bins
        counter = 0
        binRange=[]
        binValues=[]
        while counter < bins:
                binRange.append(min+((counter+1)*range))
                binValues.append(0)
                counter = counter + 1
                
        for value in aValues:
                counter = 0
                while counter < bins:
                        if value <= binRange[counter]:
                                binValues[counter] = binValues[counter] + 1
                                break
                        counter = counter + 1


        counter = 0
        maxBin = 0
        while counter < bins:
                print repr(int(binRange[counter])) + "," + repr(int(binValues[counter]))
                if ( maxBin < int(binValues[counter])):
                        maxBin = int(binValues[counter])
                counter = counter + 1

        print "\n"
        counter = 0
        while counter < bins:
                line=repr(int(binRange[counter])) + "\t "
                toPrint = 0
                binRatio=int((10/float(maxBin))*float(binValues[counter]))
                while toPrint < binRatio:
                        line = line + "-"
                        toPrint = toPrint + 1
                print line + "*"
                counter = counter + 1

values=tuple(open('/bootflash/buffer.inmem.txt','r'))

minValue=46080
maxValue=0
bufferValues=[]
for value in values:
        f, m, buffer=value.rpartition(',')
        iBuffer=int(buffer.rstrip())
        bufferValues.append(iBuffer)
        if minValue > iBuffer:
                minValue = iBuffer
        if maxValue < iBuffer:
                maxValue = iBuffer

print "\n"

try:
        buckets = sys.argv[1]
except:
        pass

hist(bufferValues, int(buckets), 0, 50000)