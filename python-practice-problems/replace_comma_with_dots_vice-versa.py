def swapCommaAndDot(s):
    s = s.replace(',', 'TEMP_COMMA')
    s = s.replace('.', ',')
    s = s.replace('TEMP_COMMA', '.')
    return print(s)

swapCommaAndDot('1,234.56')
