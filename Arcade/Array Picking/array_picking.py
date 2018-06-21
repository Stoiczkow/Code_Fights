def arrayPacking(a):
    result = ''
    for el in a[::-1]:
        print(bin(el)[2:])
        result += "{0:{fill}8b}".format(el, fill='0')
    return int(result, 2)
