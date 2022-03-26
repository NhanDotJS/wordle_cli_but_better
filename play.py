#!/usr/bin/env python3

import random
import wordle


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


''')  # noqa

validWordListFile = './valid-wordle-words.txt'
with open(validWordListFile, 'r') as f:
    validWordList = f.read().split('\n')


def takeUserInput():
    while True:
        guess = input('Please type in your guess: ').lower()
        if len(guess) != 5:
            print('Your guess must be 5 characters')
        elif guess not in validWordList:
            print('Your guess is not in wordlist')
        else:
            return guess


# game = wordle.WordleGame(random.choice(validWordList), validWordList)
game = wordle.WordleGame("nolos", validWordList)
game.printOutput()

while game.checkGameCondition() == 'Ongoing':
    result = game.guess(takeUserInput())
    game.printOutput()
    if result == "Won":
        print('''
__   _______ _   _   _    _  _____ _   _ 
\ \ / /  _  | | | | | |  | ||  _  | \ | |
 \ V /| | | | | | | | |  | || | | |  \| |
  \ / | | | | | | | | |/\| || | | | . ` |
  | | \ \_/ / |_| | \  /\  /\ \_/ / |\  |
  \_/  \___/ \___/   \/  \/  \___/\_| \_/
                                         
                                         ''')  # noqa
        break
    elif result == "Lost":
        print('''
__   _______ _   _   _     _____ _____ _____ 
\ \ / /  _  | | | | | |   |  _  /  ___|_   _|
 \ V /| | | | | | | | |   | | | \ `--.  | |  
  \ / | | | | | | | | |   | | | |`--. \ | |  
  | | \ \_/ / |_| | | |___\ \_/ /\__/ / | |  
  \_/  \___/ \___/  \_____/\___/\____/  \_/  
                                             
                                         ''')  # noqa
        print(f'The word is: {game.answer}')
        break
