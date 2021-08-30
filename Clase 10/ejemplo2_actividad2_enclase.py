# Crear un diccionario con los nombres de los departamentos como
# keys y una lista con los municipios como value. Para probar el 
# resultado pida con input un nombre de un departamento e imprima 
# sus municipios
import csv

file = open("Municipality_Area.csv", encoding='UTF-8')

# read forma 2
lines = csv.DictReader(file, delimiter=',')

depmun = {}
listamun = []
i = 0
for aux in lines:
   if i==0:
       depAnt = aux['Departamento']
   dep = aux['Departamento']
   mun = aux['Municipio']
   i = i + 1
   if dep == depAnt:
       listamun.append(mun)
   else:
       depmun[depAnt] = listamun
       i = 0
       listamun = []
       listamun.append(mun)
depsearch = input("Indique el nombre del departamento: ")
print(depmun[depsearch])
