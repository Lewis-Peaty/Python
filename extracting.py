import time
import random

numDataSets = 1001
for a in range(1,numDataSets):
    r = random.randint(1,10)
    for p in range(0,1000,r):
        print "Extracting " + str(a) + " of " + str(numDataSets-1) + ": " + str(float(p)/10) + "% " + "Complete."
        time.sleep(float(r)/10)
    print "Extracting "  + str(100) + "% " + "Complete."
print "..."
print "Extracting Completed Successfully!"
