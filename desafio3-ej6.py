
""" 6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto)) """

lista_0_10 = list(range(0, 11))
lista_10_0 = list(range(-10, 1))
lista_pares = list(range(0, 21, 2))
lista_impares = list(range(-19, 0, 2))
lista_mult_5 = list(range(5, 51, 5))

print(f"Lista 0-10: {lista_0_10}")
print(f"Lista -10-0: {lista_10_0}")
print(f"Lista pares: {lista_pares}")
print(f"Lista impares: {lista_impares}")
print(f"Lista mult 5: {lista_mult_5}")

# Nota: creo que el cero no es múltiplo de 5 como figura en el ejemplo, por eso no lo agregué a la lista.
