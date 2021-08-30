# Separar los datos del archivo Municipality_Area.csv
# en tres arreglos, uno por columna. Para texto usar
# listas y para número ndarray de numpy. Luego:
# a. ¿cuál es el área total de Colombia?
# b. ¿cúal es el municipio de mayor área en Colombia?
# c. ¿cuántos departamentos tiene Colombia?

import csv
import numpy as np

file = open("Municipality_Area.csv", encoding='UTF-8')
lines = list(csv.reader(file, delimiter=','))

# quitemos los headers
del lines[0]

# creamos las variables
areas = np.ones(len(lines))
dep = []
mun = []

# llenamos las variables
i = 0
for aux in lines:
    dep.append(aux[0])
    mun.append(aux[1])
    try:
        areas[i] = int(aux[2])
    except:
        areas[i] = 0
    i = i + 1

# a
print(np.sum(areas))

# b
indMax = np.argmax(areas)
print(lines[indMax])
print(mun[indMax])

# c
uniquedep = set(dep)
print(f"numero de departamentos: {len(uniquedep)}")
print(set(dep))

