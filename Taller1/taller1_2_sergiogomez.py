import os

files = os.listdir('./archivos_discharge_s')

def palabra(path):
    palabras = ["tracheotomy", "tracheostomy", "Tracheotomy", "Tracheostomy"]
    with open('./archivos_discharge_s/' + path) as infile:
        for line in infile:
            line = line.lower()
            for track in palabras:
                palabra = line.find(track)
                if palabra != -1:
                    return "la palabra si se encuentra"
        return "la palabra no se encontro"
print("selecione un archivo")
for index, pablo in enumerate (files):
    print(index+1, pablo)

file = input()

try:
    file= int(file)
    print(palabra(files[file-1]))
except:
    print("Archivo no encontrado")