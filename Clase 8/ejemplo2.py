import csv

#forma 1
#file = open ("Municipality_Area.csv", encoding = 'UTF-8') #los caracteres no los reconoce y se pone este file 
# lines = csv.reader(file, delimiter = ",")
# lines = list(lines)
# print (lines)
# print (lines[3][1])


#forma 2
file = open ("Municipality_Area.csv", encoding = 'UTF-8')
lines = csv.DictReader(file, delimiter=",")
for aux in lines:
    print(aux)
    print(aux['Municipio'])

file.close()
