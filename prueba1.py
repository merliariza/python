#Ejercicio que solicita la información de 5 sismos para 5 departamentos, en base a eso
promedioSismos=0
totalDep=5
totalmuestras= 5
depMayorRiesgo=''
depMenorRiesgo=''
depsinRiesgo=''
mayorRiesgo = 0
menorRiesgo = float('inf')

for i in range(0,totalDep):
    nombreDep= input(f'Ingrese el nombre del departamento')
    sumaMuestras=0
    for i in range(0,totalmuestras):
        muestra= float(input(f'Ingrese la muestra del sismo para el departamento {nombreDep}'))
        sumaMuestras += muestra
        promedioSismos = (sumaMuestras/totalmuestras)
    print(f'El promedio del departamento {nombreDep} es de {promedioSismos}')
    if promedioSismos >=8.0 :
         print ('El riesgo de sismo es alto')
    elif promedioSismos <3.0 :
         print ('No hay riesgo de sismo')
    if 8.0>promedioSismos>=3.0 :
         print ('El riesgo de sismo es bajo')


    if promedioSismos > mayorRiesgo:
        mayorRiesgo = promedioSismos
        depMayorRiesgo = nombreDep
    
    if promedioSismos < menorRiesgo:
        menorRiesgo = promedioSismos
        depMenorRiesgo = nombreDep

if depMayorRiesgo:
    print(f'El departamento con mayor riesgo es {depMayorRiesgo} con un promedio de {mayorRiesgo}')
if depMenorRiesgo:
    print(f'El departamento con menor riesgo es {depMenorRiesgo} con un promedio de {menorRiesgo}')
if depsinRiesgo:
    print(f'Los departamentos sin riesgo son: {depsinRiesgo}')