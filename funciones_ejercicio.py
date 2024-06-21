import os, time, msvcrt, csv
ventas=[]
letras=["A","B","C","D", "E"]
asientos=[[a for a in range(1,11)] for x in range (5)]

def opc_1():
    print("\tASIENTOS DISPONIBLES\n")
    print(" -"+"-"*33+"- ")
    for x in range(len(asientos)):
        print("|",letras[x],asientos[x],"|")
    print(" _"+"_"*33+"_ ")

def opc_2():
    print("\tCOMPRAR ENTRADAS\n")
    while True:
        asiento_letra=input("Ingrese la letra del asiento (A, B, C, D o E): ")
        for x in letras:
            if x==asiento_letra.upper():
                break
        if x==asiento_letra.upper():
            numero_x=letras.index(asiento_letra.upper())
            break
        else:
            print("Error, debe ingresar una letra correcta!")  
            time.sleep(2)
    while True:  
        try:   
            asiento_numero=int(input("Ingrese el número del asiento: "))
            if asiento_numero in asientos[0]:
                numero_y=asiento_numero-1
                break
            else:
                print("Error! Debe ingresar un número del 1 al 10!")
        except:
            print("Error! Debe ingresar un número entero!")
    if asientos[numero_x][numero_y]=="X":
        print("Error! asiento ocupado!")
        time.sleep(2)
    else:
        nombre=input("Ingrese su nombre: ")
        edad=int(input("Ingrese su edad: "))
        telefono=int(input("Ingrese su teléfono: "))
        venta={
            "nombre":nombre,
            "edad":edad,
            "telefono":telefono,
            "asiento":asientos[numero_x][numero_y]
        }
        asientos[numero_x][numero_y]="X"
        ventas.append(venta)

def opc_3():
    for v in ventas:
        print(f"")


def opc_5():
    print("Hasta la próxima!")
    exit()