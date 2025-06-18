def zip(a, b):
    print(f'Zipping {a} and {b}')
    return a+b

def unzip(a):
    print(f'Unzipping {a}')
    return a[:len(a)//2], a[len(a)//2:]