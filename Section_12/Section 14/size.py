import sys


def my_range(n: int):
    start = 0
    while start < n:
        yield start
        print('now i will increment the value')
        start += 1


big_range = my_range(5)
print(next(big_range))
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range

big_list = list(big_range)

print("big_list is {0} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)
