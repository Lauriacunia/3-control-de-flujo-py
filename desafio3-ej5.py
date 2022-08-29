""" Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso.
 Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista(devuelve True o False)
numeros = [1, 3, 6, 9]
 """

is_valid = False
list = [1, 3, 6, 9]


def is_valid_input(n):
    if not n:
        return False
    elif not n.isdigit():
        return False
    else:
        n = int(n)
        if not n >= 0 and n <= 9:
            return False
        else:
            return True


def check_if_is_in_list(n):
    if n in list:
        print("✅ El número ingresado se encuentra en la lista")
    else:
        print("🚫 El número ingresado no se encuentra en la lista")


def run():
    global is_valid
    n = input("Ingrese un número del 0 al 9: ")
    is_valid = is_valid_input(n)
    while not is_valid:
        n = input("🚫 Error. Por favor ingrese un número del 0 al 9: ")
        is_valid = is_valid_input(n)

    check_if_is_in_list(int(n))


run()
