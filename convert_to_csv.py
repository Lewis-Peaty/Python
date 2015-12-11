for num in range(1,9):
    input_file = open('DISPATCH_' + str(num) + '.gen', 'r')
    output_file = open('DISPATCH_' + str(num) + '.csv', 'w')
    input_file.readline() # skip first line 
    for line in input_file:
        commaSeparatedValues = line.strip().split()    
        output_file.write(','.join(commaSeparatedValues) + '\n')
    input_file.close()
    output_file.close()

input_file.close()
output_file.close()
print "convert_to_csv.py completed"
