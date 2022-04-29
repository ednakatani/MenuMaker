import menumaker

def sum():
    a = int(input('a: '))
    b = int(input('b: '))
    print(a+b)
    return a+b

def multiply():
    a = int(input('a: '))
    b = int(input('b: '))
    print(a*b)
    return a*b


m = menumaker.Menu("CALCULATOR",True,False,True ,[["Sum",sum],["Multiply",multiply]])


m.menu()