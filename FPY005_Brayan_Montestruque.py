import csv
import random

trabajadores = {
    "Juan Pérez" : 0,
    "María García" : 0,
    "Carlos López" : 0,
    "Ana Martínez" : 0,
    "Pedro Rodríguez" : 0,
    "Laura Hernández" : 0,
    "Miguel Sánchez" : 0,
    "Isabel Gómez" : 0,
    "Francisco Díaz" : 0,
    "Elena Fernández" : 0
    }

def sueldos_aleatorios (trabajadores):
    for trabajador, sueldo in trabajadores.items ():
        sueldo_ale = random.randint (300000, 2500000)
        trabajadores [trabajador] = sueldo_ale
    print ("Sueldos asignados.")
    print ()

def clasificar_sueldos (trabajadores):
    clasificacion = {"Menor a $800mil" : {}, "Entre $800mil y $2mill" : {}, "Mayor a 2mill" : {}}
    for trabajador, sueldo in trabajadores.items ():
        if sueldo < 800000:
            clasificacion ["Menor a $800mil"][trabajador] = sueldo
        elif sueldo < 2000000:
            clasificacion ["Entre $800mil y $2mill"][trabajador] = sueldo
        else:
            clasificacion ["Mayor a 2mill"][trabajador] = sueldo

    total_sueldos = sum (trabajadores.values ()) 
    for categoria, empleados in clasificacion.items ():
        print (f"{categoria}: ")
        print ()
        for empleado, sueldo in empleados.items ():
            print (f" {empleado} - ${sueldo}")
        print ()
        print (f"Total de personas en {categoria}: {len(empleados)}")
        print ()
    print (f"Total de sueldos: {total_sueldos}")
    print ()

def ver_estadisticas (trabajadores):
    sueldos = list (trabajadores.values ())
    sueldo_mas_bajo = min (sueldos)
    print (f"Sueldo mas bajo: {sueldo_mas_bajo}")
    sueldo_mas_alto = max (sueldos)
    print (f"Sueldo mas alto: {sueldo_mas_alto}")
    promedio_sueldos = sum (sueldos) / len(sueldos)
    print (f"Promedio Sueldos: {promedio_sueldos:.1f}")
    print ()

def reporte_sueldos (trabajadores):
    with open ('trabajadores.csv', mode='w', newline='') as file:
        writer = csv.writer (file)
        writer.writerow (["Nombre", "Sueldo Base", "Desc. Salud", "Desc. AFP", "Sueldo Liquido"])
        for trabajador, sueldo_base in trabajadores.items ():
            desc_salud = sueldo_base * 0.07
            desc_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - desc_salud - desc_afp
            writer.writerow ([trabajador, sueldo_base, desc_salud, desc_afp, sueldo_liquido])

            print (f"Nombre Empleado: {trabajador}")
            print (f"Sueldo Base: {sueldo_base:.0f}")
            print (f"Descuento Salud: {desc_salud:.1f}")
            print (f"Descuento AFP: {desc_afp:.1f}")
            print (f"Sueldo Liquido: {sueldo_liquido:.0f}")
            print ()
    print ("[!] Se han mostrado los datos y se ha importado exitosamente")
    print ()


while True:
    print ("1. Asignar sueldos.")
    print ("2. Clasificar Sueldos.")
    print ("3. Ver estadisticas.")
    print ("4. Reporte de sueldos.")
    print ("5. Salir.")
    opcion = input ("Ingrese su opcion: ")
    print ()

    if opcion == "1":
        sueldos_aleatorios (trabajadores)
    elif opcion == "2":
        clasificar_sueldos (trabajadores)
    elif opcion == "3":
        ver_estadisticas (trabajadores)
    elif opcion == "4":
        reporte_sueldos (trabajadores)
    elif opcion == "5":
        print ("Finalizando programa....")
        print ("Desarrollado por Brayan Montestruque")
        print ("RUT 22.337.478-6")
        print ()
        break
    else:
        print ("Opcion invalida.")
        print ()
