#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.

#Palabra 1: edificio
#Palabra 2: tren
#La palabra edificio tiene 4 letras mas que tren.
#Palabra 1: sol
#Palabra 2: paralelepipedo
#La palabra paralelepipedo tiene 11 letras mas que sol#

print ("Exercise 4 Longest word")

word1 = input("insert a word 1: ")
word2 = input("insert a word 2: ")

len1 = len(word1)
len2 = len(word2)

if len1 > len2 :
    dif1 = len1 - len2
    print (f"The word {word1} hace {dif1} letters more than {word2}")
elif len2 > len1: 
    dif2 = len2 - len1
    print (f"The word {word2} have {dif2} letters more than {word1}")
else: 
    print (f"both words have the same number of letters")