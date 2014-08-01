gpas = {'Lassoff': 3.12, 'Johnson': 2.22, 'Reich': 3.59, 'Honeychurch': 2.98, 'Maini': 3.11, 'Levin': 2.88, 'Marcus': 2.77, 'Banks': 3.71 }

for item in gpas:
    print "Last name:", item, ", GPA:", gpas[item]

Sum = sum(gpas.values())
Average = Sum / len(gpas)
 
print "Average GPA:", Average
