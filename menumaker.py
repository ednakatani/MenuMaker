from os import system, name
  
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class Menu:
    def __init__(self, title, clear, items):
        '''
        Title → string\n
        Clear → True for clearing screen before every menu print\n
        Items → list [ ["Item", function_name], ... ]
        
        '''
        self.title = title
        self.items = items

    def print(self):
        size = len(self.title)
        star = "*" * size * 3
        print(star)
        print("*".ljust(int(len(star) / 3)) + self.title + "".ljust(int(len(star) / 3) - 1) + "*")
        print(star)
        print()
        for item in range(len(self.items)):
            print('[' + str(item) + '] - ' + self.items[item][0])

    def get_op(self):
        self.print()
        op = input("> ")
        op = int(op)

        return op

    def menu(self):
        show = True
        while show:
            if clear:
                clear()

            op = self.get_op()
            if clear:
                clear()
            self.items[op][1]()
            input("ENTER for return")



