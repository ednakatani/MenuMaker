import menumaker

def soma():
    a = int(input('a: '))
    b = int(input('b: '))
    print(a+b)
    return a+b

def multiplica():
    a = int(input('a: '))
    b = int(input('b: '))
    print(a*b)
    return a*b


m = menumaker.Menu("CALCULADORA",True ,[["Soma",soma],["Multiplica",multiplica]])

m.menu()