""" 1)🚀 Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
    Mostrar una suma de los dos números
    Mostrar una resta de los dos números(el primero menos el segundo)
    Mostrar una multiplicación de los dos números
    Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
    En caso de no introducir una opción válida, el programa informará de que no es correcta.
 """

# SOLUCIÓN con WHILE
running = True


def is_valid_input(*args):
    # podrían agregarse mas validaciones...
    for arg in args:
        if not arg.isdigit():
            return False
    return True


def show_options():
    return input("📝 ¿Qué operación desea realizar? : 1- Suma, 2- Resta, 3- Multiplicacion, 4- Salir: ")


def sumar(n1, n2):
    print(f"✅ La suma de {n1} y {n2} es: {n1 + n2}")


def restar(n1, n2):
    print(f"✅ La resta de {n1} y {n2} es: {n1 - n2}")


def go_exit():
    global running
    exit = input("🔁 ¿Desea realizar otra operación? (S/N): ")
    if exit == "S" or exit == "s":
        return True
    else:
        print("👋 Gracias por utilizar el programa")
        running = False
        return False


def welcome():
    print("====================================================")
    print(" Bienvenido al programa de operaciones aritméticas  ")
    print("====================================================")


def calculate():
    global running
    while running:
        n1 = input("📲 Ingrese el primer numero: ")
        n2 = input("📲 Ingrese el segundo numero: ")
        if is_valid_input(n1, n2):
            n1, n2 = int(n1), int(n2)
            option = show_options()
            if is_valid_input(option):
                option = int(option)
                if option == 1:
                    sumar(n1, n2)
                    go_exit()
                elif option == 2:
                    restar(n1, n2)
                    go_exit()
                elif option == 3:
                    print(
                        "🔕 Lo sentimos: Operación no disponible. 👋Saliendo del programa...")
                    running = False
                elif option == 4:
                    print("👋 Gracias por utilizar el programa")
                    running = False
                else:  # option != 1, 2, 3, 4
                    print("🔕 Lo sentimos, opción no válida.")
                    go_exit()
            else:  # option not a number
                print("🔕 Lo sentimos, opción no válida.")
                go_exit()
        else:  # n1 or n2 not a number
            print("🔕 Error, ingrese números válidos por favor")
            calculate()


def run():
    welcome()
    calculate()


run()

# Consulta !!: no se si es necesario poner un break en el while luego de setear running = False
