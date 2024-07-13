def spin_words(sentence):
    a = sentence.split()
    b = []
    for i in a:
        if len(i) >= 5:
            i = i[::-1]
            b.append(i)
        else:
            b.append(i)
    return ' '.join(b)

print(spin_words('This is another text'))