import random
i=0
j=0
while i<1000:
    while j<100:
        print "Processing chunk " + str(i) + " of 1000. " + str(j) + "% complete."
        j = j + random.randint(0,5)
        
    
