#Realizar un programa que permita leer las notas de un estudiante y calcular la nota final y determinar si approbo o no aprobo la materia.
#La universidad por reglamento determina que cada estudiante debe presentar 3 parciales 4 quices y 2 trabajos. los parciales=60%, quices=30%, trabajos=10%


totalQuices = 4
totalTrabajos = 2
totalParciales = 3


sumaQuices = 0
sumaTrabajos = 0
sumaParciales = 0


for i in range(1, totalQuices + 1):
    quices = float(input(f'Escriba la nota {i} de quices: '))
    sumaQuices += quices


for i in range(1, totalTrabajos + 1):
    trabajos = float(input(f'Escriba la nota {i} de trabajos: '))
    sumaTrabajos += trabajos


for i in range(1, totalParciales + 1):
    parciales = float(input(f'Escriba la nota {i} de parciales: '))
    sumaParciales += parciales


promedioQuices = sumaQuices / totalQuices
promedioTrabajos = sumaTrabajos / totalTrabajos
promedioParciales = sumaParciales / totalParciales


notaFinal = (promedioParciales * 0.6) + (promedioQuices * 0.3) + (promedioTrabajos * 0.1)


if notaFinal >= 3.0:
    print(f'El estudiante aprobó con una nota final de {notaFinal:.2f}')
else:
    print(f'El estudiante no aprobó. Su nota final es {notaFinal:.2f}')