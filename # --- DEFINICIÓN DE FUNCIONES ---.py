# --- DEFINICIÓN DE FUNCIONES ---

def sumar(primer_numero, segundo_numero):
    return primer_numero + segundo_numero

def restar(primer_numero, segundo_numero):
    return primer_numero - segundo_numero

def multiplicar(primer_numero, segundo_numero):
    return primer_numero * segundo_numero

def dividir(primer_numero, segundo_numero):
    if segundo_numero == 0:
        return "Error: No se puede dividir entre cero"
    return primer_numero / segundo_numero

def es_par(numero):
    if numero % 2 == 0:
        return f"El número {numero} es PAR"
    else:
        return f"El número {numero} es IMPAR"


# --- BUCLE DEL MENÚ ---

while True:
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Verificar si un número es par")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            print("Resultado:", sumar(n1, n2))

        case "2":
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            print("Resultado:", restar(n1, n2))

        case "3":
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            print("Resultado:", multiplicar(n1, n2))

        case "4":
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            print("Resultado:", dividir(n1, n2))

        case "5":
            num = int(input("Ingresa un número entero: "))
            print(es_par(num))

        case "6":
            print("¡Gracias por usar la calculadora! Saliendo...")
            break  # Detiene el bucle 'while' y termina la ejecución

        case _:
            print("Opción inválida. Selecciona un número del 1 al 6.")