#hangman game
import random

def hangman():

    words = ['bob','steve','cat']

    name = input("what is your name? ")

    print('Welcome ' + name + ' to the hangman game!. ')

    secretword = random.choice(words)

    dashes = '-' * len(secretword)
    guess = 10

    while guess > -1 and not dashes == secretword:
        print('You have total of: ' + str(guess) + ' guesses')
        print(dashes)
        userguess = input('Enter a letter: ')
        if userguess in secretword:
            dashes = dashes_update(secretword, dashes, userguess)
            print('Good job. Your letter is in the secret word. You have: ' + str(guess) + ' guesses')
            print(dashes)
            continue
        elif len(userguess) != 1:
            print('Only enter one letter please')
            continue
        else:
            guess -= 1
            print('Letter not in the sceret word. You have: ' + str(guess) + ' guesses')
            continue

    if guess < 0:
        print("you lose. the word was " + str(secretword))

    else:
        print('congrats the word is ' + str(secretword))

def dashes_update(secret,dash,guess):
    result = ""
    for i in range(len(secret)):
        if secret[i] == guess:
            result = result + guess
        else:
            result = result + dash[i]
    return result

hangman()
