def myfun(n):
    return lambda a:a*n
doublenum=myfun(2)
triplenum=myfun(3)
print(doublenum(2))
print(triplenum(3))