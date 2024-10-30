print (f"Exercise 3 division")

D1 = int(input("insert number: "))
D2 = int(input("Insert number: "))

Co = D1 // D2
Rest = D1 % D2

if Rest == 0:
    print (f"The division is exact.")
else: 
    print (f"The division isn't exact.")
    print (f"quotient: {Co}")
    print (f"Rest {Rest}")