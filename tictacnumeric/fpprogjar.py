def tictac():
    finish=0
    board = [None] + list(range(1, 10))
  
    def draw():
        print(board[7], board[8], board[9])
        print(board[4], board[5], board[6])
        print(board[1], board[2], board[3])
        print()

    def choose_number():
        while True:
            try:
                draw()
                a = int(input())
                print("pick your number")
                b = int(input())
                if a in board:
                    return a,b
                else:
                    print("\nInvalid move. Try again")
            except ValueError:
               print("\nThat's not a number. Try again")

    def is_game_over():
       
        if finish == 9:
            print("game over\n")
            return True

    for player in 'XO' * 9:
        
        draw()
        if is_game_over():
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