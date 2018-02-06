def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin + text)


def centre_text(text):
    text = str(text)
    width = 80
    left_margin = max((width - len(text)) // 2, 0)
    print(" " * left_margin + text)


python_food()
centre_text(11309)