from os import system, name
  
def cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class Menu:
    
    def __init__(self, title: str, clear: bool, submenu: bool, wait:bool, items=[]):
        '''
        Title → string\n
        Clear → True for clearing screen before every menu print\n
        Sub → True for a submenu config\n
        Wait → True for wait input to return\n
        Items → list [ ["Item", function_name], ... ]
        
        '''
        self.clear = clear
        self.title = title
        self.submenu = submenu
        self.wait = wait
        self.items = items


    def add(self, item:list):
        self.items.append(item)

    
    def add(self, name, function):
        item = [name,function]
        self.items.append(item)


    def print(self):
        size = len(self.title)
        star = "*" * size * 3
        n_items = len(self.items)
        
        print(star)
        print("*".ljust(int(len(star) / 3)) + self.title + "".ljust(int(len(star) / 3) - 1) + "*")
        print(star)
        print()
        for item in range(n_items):
            print('[' + str(item) + '] - ' + self.items[item][0])
        if self.submenu:
            print("[" + str(n_items) + "] - Back")
        else:
            print("[" + str(n_items) + "] - Exit")


    def get_op(self):
        correct = False
        while not correct:
            try:
                cls()
                self.print()
                op = input("> ")
                op = int(op)
                correct = True
            except:
                print("ERROR")
        return op


    def menu(self):
        show = True
        while show:
            
            if self.clear:
                cls()

            op = self.get_op()
            if op == len(self.items):
                break
            if self.clear:
                cls()

            self.items[op][1]()

            if self.wait:
                input("ENTER to return")
