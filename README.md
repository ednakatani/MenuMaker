# MenuMaker
A simple terminal based menu for python applications.

![image](https://user-images.githubusercontent.com/55983395/165964056-13231dd1-7758-48df-b127-e07182714f17.png)


## Code Example: basic calculator


Importing the package:

```python
import menumaker
```

Defining the functions:

```python
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
```

Initializing the Menu class:

```python
m = menumaker.Menu("CALCULATOR",True,False,True ,[["Sum",sum],["Multiply",multiply]])
```

Once the menu is created, run it:

```python
m.menu()
```
