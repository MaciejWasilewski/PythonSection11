def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin + text)


def centre_text(*args, sep=' ', end='\n'):
    args = list(map(str, args))
    text = str(sep).join(args)
    # for arg in args:
    #     text += str(arg) + " "
    # text = str(text)
    width = 80

    left_margin = max((width - len(text + end) + (end.count("\t") + end.count("\n")) * 2) // 2, 0)
    return " " * left_margin + text


# with open("centered", mode="w") as centered_file:
#     centre_text(11309, 35, sep=";fkdjf;", end='dupa', file=centered_file)

print(centre_text("spam"))
print(centre_text("spam and bacon", 3, 4, sep=", "))
