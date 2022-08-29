"""  2) Escribí un programa que lea un número impar por teclado. 
Si el usuario no introduce un número impar, debe repetirse el 
proceso hasta que lo introduzca correctamente.
"""
is_valid = False


def is_valid_input(n):
    if not n:
        return False
    elif not n.isdigit():
        return False
    else:
        n = int(n)
        if n % 2 == 0:
            return False
        else:
            return True


def run():
    global is_valid
    n = input("Ingrese un número impar: ")
    is_valid = is_valid_input(n)
    while not is_valid:
        n = input("🚫 Error. Por favor ingrese un número impar válido: ")
        is_valid = is_valid_input(n)
    print("✅ El número impar ingresado es: ", n)


run()
