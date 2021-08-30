# Crear un diccionario con los nombres de los municipios como
# keys y el área como value. Para probar el resultado pida con input
# un nombre de un municipio e imprima su área
import csv

file = open("Municipality_Area.csv", encoding='UTF-8')

munAreas = {} 

lines = csv.DictReader(file, delimiter=',')
for aux in lines:
   mun = aux['Municipio']
   area = aux['Area (km2)']
   munAreas[mun] = area

munsearch = input("Indique el nombre del municipio: ")
print(munAreas[munsearch])