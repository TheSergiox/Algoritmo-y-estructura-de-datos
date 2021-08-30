import csv
file = open ("Municipality_Area_mod.csv", encoding = 'UTF-8')
lines = csv.DictReader(file, delimiter=",")
for aux in lines:
    print(aux)
    print(aux['Municipio'])

file.close()