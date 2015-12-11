import os
for num in range(1,9):
    input_file = open('DISPATCH_' + str(num) + '.gen', 'r')
    if os.path.exists('TIME_SERIES_' + str(num) + '.csv'): #overwrite existing
        os.remove('TIME_SERIES_' + str(num) + '.csv')
    output_file = open('TIME_SERIES_' + str(num) + '.csv', 'w')
    timeSeriesFound = False
    for line in input_file:
        commaSeparatedValues = line.strip().split()        
        if len(commaSeparatedValues)>1 and commaSeparatedValues[0] == "TIME" and commaSeparatedValues[1] == "FREQ":
            timeSeriesFound = True
        if timeSeriesFound and len(commaSeparatedValues)>20: #magic number to filter out non-numerical rows
            output_file.write(commaSeparatedValues[0] + ','+ commaSeparatedValues[1] + '\n')
    input_file.close()
    output_file.close()

    #Clean up
    os.remove('DISPATCH_' + str(num) + '.gen')
    os.remove('DISPATCH_' + str(num) + '.dat')
    os.remove('DISPATCH_' + str(num) + '.out')
    os.remove('DISPATCH_' + str(num) + '.prn')
    os.remove('DISPATCH_' + str(num) + '.rnd')
    os.remove('DISPATCH_' + str(num) + '.sum')
    

input_file.close()
output_file.close()
print "script completed"
