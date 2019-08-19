import choose_word
gallow=["                             ",
        "-------------                ",
        "|           |                ",
        "|           0                ",
        "|          /|\               ",
        "|          / \               ",
        "|                            ",
        "_____________________________"]
def maingame():
    win=False
    main_word=choose_word.board_main()
    amount = len(main_word)
    main_word=list(main_word)
    board=len(main_word)*' _ '
    board=list(board)
    print("Welcome to the game")
    errors=0
    while(errors<len(gallow)-1):
        print(''.join(board))
        print("input letter")
        char=input()
        if char in main_word:
            ind=main_word.index(char)
            main_word[ind]=''
            board[ind*3+1]=char
            amount-=1
        else:
            errors+=1
        print('\n'.join(gallow[0:errors]))
        if(amount==0):
            win=True
            print("You win")
            break
    if(win ==False):
        print("you lose")
maingame()