import random
def hangman(word):
    wrong = 0
    stages = ["",
             "__________          ",
             "|                   ",
             "|         |         ",
             "|         0         ",
             "|        /|\        ",
             "|        / \        ",
             "|                   "
             ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("I want to play a game with you!")
    while wrong < len(stages) - 1:
        print("\n")
        sentence = input("Введите букву: ")
        if sentence in rletters:
            clever = rletters.index(sentence)
            board[clever] = sentence
            rletters[clever] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))у
        if "__" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Вы проиграли! Было загадано слово: {}.".format(word))

n = random.randint(0,15)
words = ("компьютер", "мышка", "принтер",
         "скакалка", "дождь", "свитер",
         "папугай", "пчела", "телефон",
         "клавиатура", "книга", "азбука",
         "синица", "доллар", "площадь" )
hangman(words[n])
            
            
        
