#!/usr/bin/env python3

import random
import wordle
import botplayer


validWordListFile = './valid-wordle-words.txt'
with open(validWordListFile, 'r') as f:
    validWordList = f.read().split('\n')

wins = 0
total = 0
first_guess_total = {}
first_guess_wins = {}
for x in range(0, 10000):
    game = wordle.WordleGame(random.choice(validWordList), validWordList)
    # game = wordle.WordleGame("dated", validWordList)
    # game.printOutput()

    player = botplayer.BotPlayer(validWordList)
    first_guess = player.generate_guess(game)
    result = game.guess(first_guess)
    while game.checkGameCondition() == 'Ongoing':
        result = game.guess(player.generate_guess(game))
        # game.printOutput()
        if result == "Won":
            if first_guess not in first_guess_wins:
                first_guess_wins[first_guess] = 1
            else:
                first_guess_wins[first_guess] += 1
            wins += 1
            break
        elif result == "Lost":
            print(f'The word is: {game.answer}')
            break
    total += 1
    print(f'Wins: {wins}/{total}')
    print(f'Win percentage: {wins/total}')

    if first_guess in first_guess_total:
        first_guess_total[first_guess] += 1
    else:
        first_guess_total[first_guess] = 1


# print(f'First guess wins: {first_guess_wins}')
# print(f'First guess total: {first_guess_total}')
with open('first_guess_wins.txt', 'w') as f:
    for key, value in first_guess_wins.items():
        f.write(f'{key}: {value/first_guess_total[key]}')
        f.write('\n')


def sort_dictionary_by_value(dictionary):
    return sorted(dictionary.items(), key=lambda kv: kv[1])


for key, value in sort_dictionary_by_value(first_guess_wins):
    print(f'{key}: {value/first_guess_total[key]}')
