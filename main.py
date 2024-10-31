print ("Exercise 7 CALCULATOR")

number1 = float(input("Insert number: "))
symbol = (input("Insert operator (+, -, *, /): "))
number2 = float(input("Insert number: "))

if symbol == "+":
    answer1 = number1 + number2
    print (f"{number1} + {number2} = {answer1}")
elif symbol == "-":
    answer2 = number1 - number2
    print (f"{number1} - {number2} = {answer2}")
elif symbol == "*":
    answer3 = number1 * number2
    print (f"{number1} * {number2} = {answer3}")
elif symbol == "/":
    if number2 !=0:
        answer4 = number1 / number2
        print (f"{number1} / {number2} = {answer4}")
else:
        print ("No valid")
        