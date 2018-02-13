def fact(n):
    """calculate n! iteratively"""

    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def fact2(n):
    """calculate n! iteratively"""

    if n > 1:
        result = n * fact2(n - 1)
    else:
        result = 1
    return result


def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1


def fib2(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for i in range(1, n):
            result = n_minus1 + n_minus2
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for i in range(2, 44, 2):
    print(i, fib2(i + 1) / fib2(i))
    # print(i, fact(i))
    # print(i, fact2(i))
