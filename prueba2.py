#Realizar un programa que permita leer las notas de un estudiante y calcular la nota final y determinar si approbo o no aprobo la materia.
#La universidad por reglamento determina que cada estudiante debe presentar 3 parciales 4 quices y 2 trabajos. los parciales=60%, quices=30%, trabajos=10%
sumaNota=0
def leerNotas(totalNotas:int,titulo:str):
    nota= 0.0
    contadorNotas= 1
    while(totalNotas>0):
        nota += float(input(f'ingrese la nota Nro {contadorNotas} de {titulo} :'))
        contadorNotas += 1
        totalNotas -= 1

def leerNotasRecursivas(totalNotas: int, titulo:str, nota: float, totalNotasActual:int):
    global sumaNota
    if totalNotas==1:
         sumaNota=0
 
    nota += float(input(f'Ingrese la nota Nro {totalNotasActual} de {titulo}'))

    sumaNota = nota 
    totalNotasActual +=1

    if(totalNotasActual<=totalNotas):
            leerNotasRecursivas(totalNotas,titulo,sumaNota,totalNotasActual)

    return sumaNota/totalNotas

    

if(__name__=="__main__"):
    sumaparciales = 0.0
    sumaquices= 0.0
    sumatrabajos= 0.0

    sumaparciales=leerNotasRecursivas(3,'Parciales',0.0,1)
    print(sumaparciales)

    sumaquices=leerNotasRecursivas(3,'quices',0.0,1)
    print(sumaquices)

    sumatrabajos=leerNotasRecursivas(3,'trabajos',0.0,1)
    print(sumatrabajos)

    notaFinal= ((sumaparciales*0.6)+(sumaquices*0.3)+(sumatrabajos*0.1))
    print(f'la nota final es: {notaFinal}')


    if notaFinal >= 3.5:
        print('Aprobo')
    elif notaFinal <3.5:
        print('Reprobo')