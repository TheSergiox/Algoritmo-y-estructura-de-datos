
import os

files = os.listdir('./archivos_discharge_s')

def sex(path):
    with open('./archivos_discharge_s/' + path) as infile:
        for line in infile:
            line = line.lower()
            sexo = line.find('sex:')
            if sexo != -1:
                line = line.replace(" ", "")
                line = line.replace("\n", "")
                print(line[-1].upper())

print('\n \n Por favor indique el numero del archivo al que desea acceder \n \n')
for index, f in enumerate(files):
    print(index+1, f) 

file = input()

try:
    file = int(file)
    sex(files[file-1])
except:
    print("Eso no es un numero")
