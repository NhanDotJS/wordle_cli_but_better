#!/usr/bin/env python3

import random


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
        self.lastGuess = ''
        self.win = False
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
            charFromGuess = list(guess)
            result = ['', '', '', '', '']
            for x in range(len(charToFind)):
                if charToFind[x] == charFromGuess[x]:
                    result[x] = Char(guess[x], 'green')
                    charToFind[x] = ''
                    charFromGuess[x] = ''
            for x in range(len(charFromGuess)):
                if charFromGuess[x] == '':
                    continue
                else:
                    if charFromGuess[x] in charToFind:
                        result[x] = Char(guess[x], 'yellow')
                        charToFind[charToFind.index(charFromGuess[x])] = ''
                    else:
                        result[x] = Char(guess[x], 'white')
            # for x in range(len(guess)):
            #     charInGuess = guess[x]
            #     formattedChar = Char(charInGuess, 'white')
            #     if charInGuess in charToFind:
            #         formattedChar = Char(charInGuess, 'yellow')
            #         for y in range(len(charToFind)):
            #             if guess[y] == charToFind[y] and x == y:
            #                 formattedChar = Char(charInGuess, 'green')
            #                 break

            #         charToFind[charToFind.index(guess[x])] = ''
            #     result.append(formattedChar)
        self.lastGuess = result
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
