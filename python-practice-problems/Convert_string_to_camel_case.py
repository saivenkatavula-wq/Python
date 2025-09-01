import re 
def to_camel_case(text):
    x = re.split("_|-", text)
    y = []
    for i in range(0 ,len(x)):
        if i == 0:
            y.append(x[i])
        else:
            y.append(x[i].title())
    final = ''.join(y)
    return final
