from trabajador import Trabajador
from adts import Array

#Leer el archivo .dat
trabajadores = []
archivo = open('junio.dat', 'rt')
for x in archivo.readlines():
    trab = []
    for j in x.strip().split(','):
        x.replace(' ', '')
        trab.append(j)
    trabajadores.append(trab)

numTrabajadores = len(trabajadores)

#Dantdo los valores a cada uno de los trabajadores.
b = Trabajador(numTrabajadores)
for i in range(1, numTrabajadores):
    b.set_item(trabajadores[i],i)

#Guardando los datos en el Array
algo = Array(numTrabajadores)
for i in range(1, numTrabajadores):
    algo.set_item(b.get_item(i), i)

#Iterando el programa
for x in range(1,algo.get_length()):

    if (int(algo.get_item(x)[6])) < 2020:
        prestaciones = (2020 - (int(algo.get_item(x)[6])))
        sueldo = (int(algo.get_item(x)[4])*276.5) + (int(algo.get_item(x)[5])) + (prestaciones * 3)

        print()
        print(f"El Trabajador {algo.get_item(x)[1]} {algo.get_item(x)[2]} {algo.get_item(x)[3]} tiene un salario de ${sueldo} mas prestaciones del {prestaciones * 3}%")

    else:
        sueldo = (int(algo.get_item(x)[4])*276.5) + (int(algo.get_item(x)[5]))
        print()
        print(f"El Trabajador {algo.get_item(x)[1]} {algo.get_item(x)[2]} {algo.get_item(x)[3]} tiene un salario de ${sueldo}")

mayor = 0
menor = 2560

for i in range(1, len(trabajadores)):
    a = int(trabajadores[i][6])

    if (a > mayor):
        mayor = a

    if (a < menor):
        menor = a

print("")
for i in range(1, len(trabajadores)):
    if (int(trabajadores[i][6]) == mayor):
        print(f"El Trabajador {algo.get_item(i)[1]} es el de mayor antiguedad {mayor}")

    elif (int(trabajadores[i][6]) == menor):
        print(f"El trabajador {algo.get_item(i)[1]} es el de menor antiguedad {menor}")
