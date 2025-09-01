def spin_words(sentence):
    x = sentence.split()
    y=[]
    for i in x:
        if len(i) >= 5:
            y.append(i[::-1])
        else:
            y.append(i)
    final = ' '.join(y)
    return final
