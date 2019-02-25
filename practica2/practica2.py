print("Determinar si el numero ingresado es primo")

m = int(2)
band = "V"

n = int(input("Ingresar algun numero:"))
while((band == "V") and (m < n)):
        if((n % m) == 0):
                band = "F"
        else:
                m = m + 1
if(band == "V"):
        print("El numero ingresado es primo")
else:
        print("El numero ingresado no es primo")



print("Genere los numeros primos menores o iguales a n que pertenece a los naturales")

m = int(2)
band = "V"

n = int(input("Ingresar algun numero entero positivo: "))
while((band == "V") and (m < n)):
        if((n % m) == 0):
                band = "F"
        else:
                m = m + 1
if(band == "V"):
        print("El numero ingresado es primo")
else:
        print("El numero ingresado no es primo")
if n > 0:
        for i in range(2,n) :
                creciente = 2
                esprimo = True
                while esprimo and creciente < i:
                        if i % creciente == 0:
                                esprimo = False
                        else:
                                creciente += 1
                if esprimo:
                        print(i,"es un numero primo")
else:
        print("El numero ingresado no es primo")



print("Minimo comun multiplo de dos enteros")
def MCM(x, y):



        if x > y:
                mayor = x
        else:
                mayor = y

        while(True):
                if((mayor % x == 0) and (mayor % y == 0)):
                        MCM = mayor
                        break

                mayor += 1

        return MCM

numero1 = int(input("Ingresar el primer numero: "))
numero2 = int(input("Ingresar el segundo numero: "))



print("Maximo comun divisor de dos enteros")

def MCD(a, b):
        resto = 0
        while(b > 0):
                resto = b
                b = a % b
                a = resto
        return a

numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))

print("El maximo comun divisor de ", numero1," y ", numero2, " es ", MCD(numero1, numero2))

