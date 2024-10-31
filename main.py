from time import localtime

print ("Exercise 8 AGE")

day = int(input("Please, enter your day of birth: "))
month = int(input("Please, enter your nonth of birth: "))
year = int(input("Please, enter your year of birth: "))

t = localtime()
actual_day = t.tm_mday
actual_month = t.tm_mon
actual_year = t.tm_year

age = actual_year - year

if (actual_month < month) or (actual_month == month and actual_day < day):
    age -=1 

print (f"you have {age} years old")
