from functools import cache
import random
import re
from tkinter import W


class BotPlayer:
    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.yellow_char = ['', '', '', '', '']
        self.green_char = ['', '', '', '', '']
        self.white_char = []

    def generate_guess(self, wordle_game):
        if wordle_game.lastGuess == "":
            return random.choice(self.wordlist)
        else:
            for char in wordle_game.lastGuess:
                if char.color == 'yellow':
                    self.yellow_char[wordle_game.lastGuess.index(char)] = char.char  # noqa
                elif char.color == 'green':
                    self.green_char[wordle_game.lastGuess.index(char)] = char.char  # noqa
            for char in wordle_game.lastGuess:
                if char.color == 'white' and char.char not in self.yellow_char and char.char not in self.green_char:  # noqa
                    self.white_char.append(char.char)

            # print(self.yellow_char, self.green_char, self.white_char)
            # print(yellow_char, green_char, white_char)
            self.wordlist = self.remove_words_with_white_chars(self.white_char, self.wordlist)  # noqa
            self.wordlist = self.find_words_with_yellow_chars(self.yellow_char, self.wordlist)  # noqa

            self.wordlist = self.remove_words_with_yellow_chars(self.yellow_char, self.wordlist)  # noqa

            self.wordlist = self.find_words_with_green_chars(self.green_char, self.wordlist)  # noqa

            for word in wordle_game.pastWords:
                if word in self.wordlist:
                    self.wordlist.remove(word)
            return random.choice(self.wordlist)

    def find_words_with_yellow_chars(self, lschar, ls):
        if lschar == []:
            return ls
        else:
            result = []
            for word in ls:
                if lschar[0] in word:
                    result.append(word)
            return self.find_words_with_yellow_chars(lschar[1:], result)

    def find_words_with_green_chars(self, lschar, ls):
        if lschar == ['', '', '', '', '']:
            return ls
        else:
            result = []
            for word in ls:
                getWord = True
                for char in lschar:
                    if char != '':
                        if word[lschar.index(char)] != char:
                            getWord = False
                if getWord:
                    result.append(word)
            return result

    def remove_words_with_yellow_chars(self, lschar, ls):
        if lschar == ['', '', '', '', '']:
            return ls
        else:
            result = ls.copy()
            for char in lschar:
                if char != '':
                    for word in ls:
                        if word[lschar.index(char)] == char:
                            if word in result:
                                result.remove(word)
            return result

    def remove_words_with_white_chars(self, lschar, ls):
        result = ls.copy()
        for word in ls:
            for char in lschar:
                if char in word:
                    if word in result:
                        result.remove(word)
        return result
