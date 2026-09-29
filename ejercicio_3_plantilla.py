try:

    numero_dia = int(input("Escribe un número del 1 al 7: "))



    match numero_dia:
        case 1:
            print("El día seleccionado es: Lunes")
        case 2:
            print("El día seleccionado es: martes")
        case 3:
            print("El día seleccionado es: miercoles")
        case 4:
            print("El día seleccionado es: jueves")
        case 5:
            print("El día seleccionado es: viernes")
        case 6:
            print("El día seleccionado es: sabado")
        case 7:
            print("El día seleccionado es: domingo")
        case _:
            print("Error: el número debe estar entre 1 y 7.")
except ValueError:
            print("Debes ingresar un numero valido")
            