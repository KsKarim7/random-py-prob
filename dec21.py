

def calc(dict):
    dct = {}
    for k, v in dict.items():
        if (k[0] == k[-1]):
            dct[k[-1]] = [v]
    return dct


dict = {'mom': 123, 'cannon': 324, 'lol': 45, 'faf': 101}
a = calc(dict)
print(a)
