#!/usr/bin/env python3

import random


print('''

 _    _  _____ ______ ______  _      _____             
| |  | ||  _  || ___ \|  _  \| |    |  ___|            
| |  | || | | || |_/ /| | | || |    | |__              
| |/\| || | | ||    / | | | || |    |  __|             
\  /\  /\ \_/ /| |\ \ | |/ / | |____| |___             
 \/  \/  \___/ \_| \_||___/  \_____/\____/             
                                                       
                                                       

                                                       
 _             _                    _____  _     _____ 
| |           | |                  /  __ \| |   |_   _|
| |__   _   _ | |_    ___   _ __   | /  \/| |     | |  
| '_ \ | | | || __|  / _ \ | '_ \  | |    | |     | |  
| |_) || |_| || |_  | (_) || | | | | \__/\| |_____| |_ 
|_.__/  \__,_| \__|  \___/ |_| |_|  \____/\_____/\___/ 


''')  # noqa # Credit to: patorjk https://patorjk.com/software/taag


class Char:
    def __init__(self, char, color):
        self.char = char
        self.color = color

    def format(self):
        if self.color == 'green':
            return f'\033[92m{self.char}\033[00m'
        elif self.color == 'yellow':
            return f'\033[93m{self.char}\033[00m'
        else:
            return self.char


win = False

# Credit:dracos https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93
validWordListFile = './valid-wordle-words.txt'
with open(validWordListFile, 'r') as f:
    validWordList = f.read().split('\n')

# answer = 'dated'
answer = random.choice(validWordList)

displayChars = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']]


# def toYellow(text):
#     return f'\033[93m{text}\033[00m'


# def toGreen(text):
#     return f'\033[92m{text}\033[00m'


def printOutput():
    print(f'''
    +---+---+---+---+---+
    | {displayChars[0][0].format()} | {displayChars[0][1].format()} | {displayChars[0][2].format()} | {displayChars[0][3].format()} | {displayChars[0][4].format()} |
    +---+---+---+---+---+
    | {displayChars[1][0].format()} | {displayChars[1][1].format()} | {displayChars[1][2].format()} | {displayChars[1][3].format()} | {displayChars[1][4].format()} |
    +---+---+---+---+---+
    | {displayChars[2][0].format()} | {displayChars[2][1].format()} | {displayChars[2][2].format()} | {displayChars[2][3].format()} | {displayChars[2][4].format()} |
    +---+---+---+---+---+
    | {displayChars[3][0].format()} | {displayChars[3][1].format()} | {displayChars[3][2].format()} | {displayChars[3][3].format()} | {displayChars[3][4].format()} |
    +---+---+---+---+---+
    | {displayChars[4][0].format()} | {displayChars[4][1].format()} | {displayChars[4][2].format()} | {displayChars[4][3].format()} | {displayChars[4][4].format()} |
    +---+---+---+---+---+
    | {displayChars[5][0].format()} | {displayChars[5][1].format()} | {displayChars[5][2].format()} | {displayChars[5][3].format()} | {displayChars[5][4].format()} |
    +---+---+---+---+---+
    ''')  # noqa


# printOutput()
def takeInput():
    while True:
        guess = input('Please type in your guess: ').lower()
        if len(guess) != 5:
            print('Your guess must be 5 characters')
        elif guess not in validWordList:
            print('Your guess is not in wordlist')
        else:
            return verifyWord(guess, answer)


def verifyWord(guess, answer):
    result = []
    if guess == answer:
        for char in guess:
            result.append(Char(char, 'green'))
        return result, True
    else:
        charToFind = list(answer)
        for x in range(len(guess)):
            charInGuess = guess[x]
            formattedChar = Char(charInGuess, 'white')
            if charInGuess in charToFind:
                if charToFind[x] == charInGuess:
                    formattedChar = Char(charInGuess, 'green')
                else:
                    formattedChar = Char(charInGuess, 'yellow')
                charToFind[charToFind.index(guess[x])] = ''
            result.append(formattedChar)
        return result, False


# for x in range(6):
#     printOutput()
#     displayChars[x], win = takeInput()
#     if win:
#         break

if win:
    printOutput()
    print('''
__   _______ _   _   _    _  _____ _   _ 
\ \ / /  _  | | | | | |  | ||  _  | \ | |
 \ V /| | | | | | | | |  | || | | |  \| |
  \ / | | | | | | | | |/\| || | | | . ` |
  | | \ \_/ / |_| | \  /\  /\ \_/ / |\  |
  \_/  \___/ \___/   \/  \/  \___/\_| \_/
                                         
                                         ''')  # noqa
else:
    printOutput()
    print('''
__   _______ _   _   _     _____ _____ _____ 
\ \ / /  _  | | | | | |   |  _  /  ___|_   _|
 \ V /| | | | | | | | |   | | | \ `--.  | |  
  \ / | | | | | | | | |   | | | |`--. \ | |  
  | | \ \_/ / |_| | | |___\ \_/ /\__/ / | |  
  \_/  \___/ \___/  \_____/\___/\____/  \_/  
                                             
                                         ''')  # noqa
    print(f'The word is: {answer}')


class WordleGame:
    def __init__(self, answer, wordList):
        self.displayChars = [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']]
        self.answer = answer.lower()
        self.lastWord = ''
        self.win = "Ongoing"
        self.pastWords = []
        self.position = 0
        self.wordList = wordList

    def printOutput(self):
        print(f'''
            +---+---+---+---+---+
            | {self.displayChars[0][0].format()} | {self.displayChars[0][1].format()} | {self.displayChars[0][2].format()} | {self.displayChars[0][3].format()} | {self.displayChars[0][4].format()} |
            +---+---+---+---+---+
            | {self.displayChars[1][0].format()} | {self.displayChars[1][1].format()} | {self.displayChars[1][2].format()} | {self.displayChars[1][3].format()} | {self.displayChars[1][4].format()} |
            +---+---+---+---+---+
            | {self.displayChars[2][0].format()} | {self.displayChars[2][1].format()} | {self.displayChars[2][2].format()} | {self.displayChars[2][3].format()} | {self.displayChars[2][4].format()} |
            +---+---+---+---+---+
            | {self.displayChars[3][0].format()} | {self.displayChars[3][1].format()} | {self.displayChars[3][2].format()} | {self.displayChars[3][3].format()} | {self.displayChars[3][4].format()} |
            +---+---+---+---+---+
            | {self.displayChars[4][0].format()} | {self.displayChars[4][1].format()} | {self.displayChars[4][2].format()} | {self.displayChars[4][3].format()} | {self.displayChars[4][4].format()} |
            +---+---+---+---+---+
            | {self.displayChars[5][0].format()} | {self.displayChars[5][1].format()} | {self.displayChars[5][2].format()} | {self.displayChars[5][3].format()} | {self.displayChars[5][4].format()} |
            +---+---+---+---+---+
            ''')  # noqa

    def guess(self, guess):
        result = []
        if guess == self.answer:
            for char in guess:
                result.append(Char(char, 'green'))
            self.win = True
        else:
            charToFind = list(self.answer)
            for x in range(len(guess)):
                charInGuess = guess[x]
                formattedChar = Char(charInGuess, 'white')
                if charInGuess in charToFind:
                    if charToFind[x] == charInGuess:
                        formattedChar = Char(charInGuess, 'green')
                    else:
                        formattedChar = Char(charInGuess, 'yellow')
                    charToFind[charToFind.index(guess[x])] = ''
                result.append(formattedChar)
        self.lastWord = result
        self.displayChars[self.position] = result
        self.pastWords.append(guess)
        self.position += 1
        return self.checkGameCondition()

    def checkGameCondition(self):
        if self.win:
            return "Won"
        elif not self.win and self.position < 6:
            return "Ongoing"
        else:
            return "Lost"


game = WordleGame('Hello')

print(game.guess('dated'))
game.printOutput()
print(game.guess('hello'))
game.printOutput()
