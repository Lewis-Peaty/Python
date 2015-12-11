import csv
with open('CGW TOTAL MEGAWATTS 3 YEARS.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     previousRowMW = 0
     for row in spamreader:
#         print ', '.join(row)
         dPdt = float(row[1]) - previousRowMW
         if dPdt > 33.3 or dPdt < -33.3:
             print row[0] + ', ' + str(dPdt) + ' MW/min'
         previousRowMW = float(row[1])


