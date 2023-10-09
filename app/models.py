class Field:
    def __init__(self, index, char, activated):
        self.index = index
        self.char = char
        self.activated = activated
    def __repr__(self):
        if self.char == '_':
            return(str(self.index))
        else:
            return self.char

class Controller:
    turn = 1
    char = ''
    occupied = 0

f = Field(1, '_', False)