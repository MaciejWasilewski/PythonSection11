n1 = (input("First number: "))
n2 = (input("Second number: "))

try:
    print("The division is {0}".format(int(n1) / int(n2)))
except (ZeroDivisionError, ValueError):
    print("It is not possible to divide these two things!")
else:
    print("Success!")
finally:
    print("End of the program")