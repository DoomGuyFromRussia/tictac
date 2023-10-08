from models import *
playerChar = 'x'
print('you will play for ' + playerChar)
fields = [[Field(1, '_', False),Field(2, '_', False),Field(3, '_', False)],
          [Field(4, '_', False),Field(5, '_', False),Field(6, '_', False)],
          [Field(7, '_', False),Field(8, '_', False),Field(9, '_', False)]]
def draw():
    for row in fields:
        print(row)

def getInput():
    index = 0
    try:
        index = int(input('enter index for your char, enter something bad if you want to quit'))
        if 1 <= index <= 9:
            for i in range(0, 2):
                for j in range(0,2):
                    if fields[(index - 1) // 3][(index - 1) % 3].char != 'x':
                        fields[(index - 1) // 3][(index - 1) % 3].char = 'x'
                        break
                    else:
                        print('this field is  already occupied')
        else:
            print('invalid value')
            return 0
    except ValueError:
        print('invalid value')
        return 0
while True:
    draw()
    if not getInput():
        break