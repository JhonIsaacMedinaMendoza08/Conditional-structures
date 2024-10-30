#Escriba un programa que determine si el número entero ingresado por el usuario es par o no.

#Ingrese un número: 4
#Su número es par
#Ingrese un número: 3
#Su número es impar
print ("Exercise 1")
number = int(input("Insert number, please: "))

if number % 2 == 0 :
    print ("The number is even")
else: 
    print("The number is odd")