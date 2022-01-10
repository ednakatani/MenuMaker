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

menu_soma = menumaker.Menu("SOMA", True, [["Soma 2",soma]])

m = menumaker.Menu("CALCULADORA",True ,[["Soma",menu_soma.menu],["Multiplica",multiplica]])


m.menu()