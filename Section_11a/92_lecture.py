def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin + text)


def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    args = list(map(str, args))
    text = str(sep).join(args)
    # for arg in args:
    #     text += str(arg) + " "
    # text = str(text)
    width = 80
    left_margin = max((width - len(text+end)) // 2, 0)
    print(" " * left_margin + text, end=end, file=file, flush=flush)


python_food()
centre_text(11309, 35, sep=";fkdjf;", end='dupa')
