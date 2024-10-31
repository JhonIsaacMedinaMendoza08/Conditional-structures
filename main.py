print ("Exercise 6 letter or number")

character = input ("insert a single character: ")

if character.isdigit():
    print ("Is a number")

elif character.isalpha(): 
    if character.isupper():
        print ("the letter is capitalized")
    else:
        print ("the letter is lowercase")
else:
    print ("It is neither a letter nor a number")