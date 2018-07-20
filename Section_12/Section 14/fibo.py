def fibo(n1, n2):
    while True:
        n2, n1 = n1 + n2, n2
        yield n2


def odd():
    n = 1
    while 1:
        yield n
        n += 2


def pi_approx():
    i = odd()
    pi = 0
    n = 1
    while 1:
        yield pi
        pi += (-1) ** (n - 1) * 4 / next(i)
        n += 1


a = fibo(1, 1)
print(next(a))
print(next(a))
a = odd()
for i in range(100):
    print(next(a))

pi = pi_approx()

for i in range(100):
    print(next(pi))
