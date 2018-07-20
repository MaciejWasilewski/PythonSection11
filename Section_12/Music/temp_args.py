# challenge


# def build_tuple(*args):
#     return args


# message_tuple = build_tuple("hello", "planet", "earth")
# print(type(message_tuple))
# print(message_tuple)
# number_tuple = build_tuple(1, 2, 3, 4, 5)
# print(type(number_tuple))
# print(number_tuple)

# kwargs

def print_backwards(*args, **kwargs):
    if kwargs.get('end'):
        pass
    else:
        kwargs['end'] = '\n'
    words=args[::-1]
    print(*words, **kwargs)


with open('backwards.txt', 'w') as backwards:
    print_backwards("hello", "word", file=backwards, sep='*')
