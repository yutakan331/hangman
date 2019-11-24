import random


def hangman():
    words = ["hello", "world", "good", "bye"]
    word = random.choice(words)
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    rletters = list(word)
    board = ["__ "] * len(word)
    win = False
    print("Welcome to Hangman!")
    while wrong < len(stages) - 1:
        # print("\n")
        msg = "Guess a letter: "
        guess = input(msg)
        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = '$'
        else:
            wrong += 1
        print(("".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__ " not in board:
            print("You WIN!!!")
            print("".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You LOSE!!! It was {}.".format(word))

hangman()