#! /usr/bin/env python2.7

print("los valores de tipo booleano son verdadero y falso y se escriben como true y false")

print("los tres tipos de operadores son or, and y not")

print("tablas de verdad or")

booleanos =[False, True]

print('x\ty\tx or y')
print('-'*19)
for x in booleanos:
    for y in booleanos:
        print(x, y, x or y)

print("tabla de verdad not")
print('x\tnot x')
print('-'*19)
for x in booleanos:
    print(x, not x)

print("tabla de verdad and")

print('x\ty\tx and y')
print('-'*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x and y)
print("son >,<,=,==,-,+")

print("el operador = asignacion le podemos dar un valor numerico a una letra o palabra y el valor == es para comparar si son dos numeros iguales por ejemplo")

print(" las condiciones son aquellas que permiten realizar discriminaciones de informacion y las usaria para realizar programas por ejemplo una calculadora")

print("para quitar lo atascado de un programa se escribe top para ver todos los procesos despues se identifica el id y se teclea kill-9 id en caso de la mac o teclear k+ id en caso de linux")

print(" romper no se evalua en el bucle despues de poner romper y continuar pasa a la siguiente iteracion del bucle")

print(" rango 10 es de donde va a iniciar , 0,10 es de donde va iniciar y a donde va terminar y por ultimo 0,10,1 el cero es donde va iniciar el 10 es donde va terminar y el 1 es que va a contar de uno en uno")

print("programa con while")
n = 1
h = ''
while n<= 10:
	print n,
	n +=1
print("programa numeros impares")

z = int(input("introduzca un numero:"))
n = 1
h = ''
while n<= z:
	if n%2 != 0:
		h += ' %i' % n
	n += 1
print h

print("programa fibonacci")
r = int(input("introduzca un numero:"))
a, b = 0,1
while b < r:
	print(b)
	a, b = b, a+b


