from funciones_ejercicio import *
while True:
    print("\tMENÚ CINE\n")
    print("1. Mostrar asientos disponibles")
    print("2. Comprar entrada")
    print("3. Mostrar ventas realizadas")
    print("4. Generar archivo CSV de ventas")
    print("5. Salir")
    opc=int(input("Ingrese el número del menú: "))
    if opc==1:
        opc_1()
    elif opc==2:
        opc_2()
    elif opc==3:
        pass
    elif opc==4:
        pass
    else:
        opc_5()