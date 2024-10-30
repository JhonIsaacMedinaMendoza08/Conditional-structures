#Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:

#Ingrese un anno: 1988
#1988 es bisiesto
#Ingrese un anno: 2011
#2011 no es bisiesto
#Ingrese un anno: 1700
#1700 no es bisiesto
#Ingrese un anno: 1500
#1500 es bisiesto

print ("Exercise 2")
year = int(input("Insert year, please: "))

if year % 400 == 0:#or year %400 ==0 :
    print ("The year is leap year")
elif year %4 ==0:
    print ("The year is leap year")
else:
    print ("The year isn't leap year")