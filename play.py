#!/usr/bin/env python3

from mimetypes import guess_all_extensions
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


game = wordle.WordleGame(random.choice(validWordList), validWordList)

while game.checkGameCondition() == 'Ongoing':
    result = game.guess(takeUserInput())
