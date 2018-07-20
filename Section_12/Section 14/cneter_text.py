text=['asdasd','sad']

text_centered=[" "*((80-len(word))//2)+word+" "*((80-len(word))//2) for word in text]

for t in text_centered:
    print(t)