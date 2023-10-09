from models import *
fields = [[Field(1, '_', False),Field(2, '_', False),Field(3, '_', False)],
          [Field(4, '_', False),Field(5, '_', False),Field(6, '_', False)],
          [Field(7, '_', False),Field(8, '_', False),Field(9, '_', False)]]
Controller.turn = 1
def start():
    ch1 = ''
    ch2 = ''
    while True:
        #print(ch1, ch2)
        ch1 = input('player 1 is choosing char (enter x or o)').lower()
        ch2 = input('player 2 is choosing char (enter x or o)').lower()
        if ch1 == 'x' and ch2 == 'o' or ch1 == 'o' and ch2 == 'x':
            break
        else:
            print('input error, try again')
    print('all players choosed characters, starting game')

def draw():
    for row in fields:
        print(row)

def checkWinner(f):
    for i in range(0, 2):
        for j in range(0, 2):
            if f[i][0].char == f[i][1].char and f[i][0].char == f[i][2].char:
                return f[i][0].char
            if f[0][i].char == f[1][i].char and f[0][i].char == f[2][i].char:
                return f[0][i].char
            if f[0][0].char == f[1][1].char and f[0][0].char == f[2][2].char:
                return f[0][0].char
            if f[0][2].char == f[1][1].char and f[0][2].char == f[2][0].char:
                return f[0][2].char

def getInput():
    print('turn', Controller.turn)
    index = 0
    Controller.char = ''
    if Controller.turn == 1:
        Controller.char = 'x'
    else:
        Controller.char = 'o'
    while True:
        try:
            inputLine = 'player ' + str(Controller.turn) + ', enter index for your char, enter something bad if you want to quit'
            index = int(input(inputLine))
            if 1 <= index <= 9:
                if fields[(index - 1) // 3][(index - 1) % 3].char != 'x' and fields[(index - 1) // 3][(index - 1) % 3].char != 'o' :
                    fields[(index - 1) // 3][(index - 1) % 3].char = Controller.char
                    if Controller.turn == 1:
                        Controller.turn = 2
                    else:
                        Controller.turn = 1
                    print ('now player ' + str(Controller.turn) + ' turn')  
                    break  
                else:
                    print('this field is  already occupied')
                    #continue
            else:
                print('invalid value')
                continue
        except ValueError:
            print('invalid value')
            continue
start()
while True:
    draw()
    getInput()
    if checkWinner(fields) == 'x' or checkWinner(fields) == 'o' :
        print (checkWinner(fields), 'won!')
        break
