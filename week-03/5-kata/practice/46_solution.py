# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate():
    def __init__(self):
        self.drunkness = 0

    def drink_rum(self):
        self.drunkness += 1

    def hows_goin_mate(self):
        if self.drunkness >= 5:
            return 'Arrrr!'
        else:
            return 'Nothin\''
