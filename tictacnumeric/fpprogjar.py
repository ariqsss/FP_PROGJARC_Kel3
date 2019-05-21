def tictac():
    finish=0
    board = [None] + list(range(1, 10))
    number = []
    sets=[
          (1,2,3),
          (4,5,6),
          (7,8,9),
          (1,4,7),
          (2,5,8),
          (3,6,9)
    ]

    def draw():
        print(board[1], board[2], board[3])
        print(board[4], board[5], board[6])
        print(board[7], board[8], board[9])
        print()

    def check_number(b):
        if b > 0 and b < 10:
            if b not in number:
                number.append(b)
                return True
            elif b in number:
                return ("\nNumber already exist. Try again")
        else:
            return ("\nIncorrect number. Try again")

    def choose_number():
        while True:
            try:
                draw()
                a = int(input())
                if a in board:
                    b = int(input("Pick your number:"))
                    number_validation = check_number(b)
                    if (number_validation == True):
                        return a,b
                    else:
                        print(number_validation)
                else:
                    print("\nField already taken. Try again")

            except ValueError:
               print("\nThat's not a number. Try again")

    def is_game_over():
       
        if finish == 9:
            print("game over\n")
            return True

    def calculate():
        maxx=0
        maxo=0
        
        for a,b,c in sets:
            scorex=0
            scoreo=0
            if 'X' in board[a]:
                scorex+=int(board[a][1])
            if 'X' in board[b]:
                scorex+=int(board[b][1])
            if 'X' in board[c]:
                scorex+=int(board[c][1])
            if 'O' in board[a]:
                scoreo+=int(board[a][1])
            if 'O' in board[b]:
                scoreo+=int(board[b][1])
            if 'O' in board[c]:
                scoreo+=int(board[c][1])
            if scorex>maxx:
                maxx=scorex
            if scoreo>maxo:
                maxo=scoreo
            print("%d %d %d : X= %d O= %d"%(a,b,c,scorex,scoreo))
        print("Player X highest score:%d\nPlayer O highest score:%d"%(maxx,maxo))
        if(maxx>maxo):
            print("X wins the game")
        if(maxo>maxx):
            print("O wins the game")
        
                
        
        
    for player in 'XO' * 9:
        
        draw()
        if is_game_over():
            calculate()
            break
        print("Player {0} pick your move".format(player))
        a,b=choose_number()
        c=str(b)
        board[a] = player+c
        finish+=1
        print()




while True:
    tictac()
    if input("Play again (y/n)\n") != "y":
        break