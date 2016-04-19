class Menu:
    def __init__(self, items):
        self.items = items

    def choose(self, number):
        for item in self.items:
            if item.num == number:
                return item.action()



