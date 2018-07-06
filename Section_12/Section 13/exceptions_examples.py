def factorial(x):
    return 1 if x<2 else x*factorial(x-1)
try:
    print(factorial(999))
except RecursionError:
    print("This program calculate factorials that are too large.")

print("End of execution.")