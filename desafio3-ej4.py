""" 4) Escribí un programa que pida al usuario cuantos números quiere introducir. 
Luego lee todos los números y realiza una media aritmética: """

qty = int(input("¿Cuántos números quiere introducir? "))
lista = range(qty)
numbers = []
for index, item in enumerate(lista):
    numbers.append(int(input(f"Introduzca número {index + 1}:  ")))
print("La media aritmética de los números introducidos es: ", sum(numbers) / qty)
