lista = ['Sergio' , 'Andrea' , 'Nicol' , 'Veronica' , 'Nicol ', 'Sara' , 'Sergio ']
b = 0
x = input('ingrese un nombre : ')
x = x.capitalize()
for i in lista: 
    if i.capitalize()==x:
        b = b + 1
print(b)