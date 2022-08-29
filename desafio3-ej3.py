""" 3) Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

    🖐 Ayuda: Podes utilizar la funciones sum() y range()
     para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto)
     indica un salto de números.
 """
numbers = list(range(1, 101, 2))
print("La suma de todos los números impares desde el 0 hasta el 100 es: ",
      sum(numbers))
