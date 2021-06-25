import json
from random import choice

if __name__ == '__main__':
    with open('words_dictionary.json', 'r') as j:
        words = [*json.load(j)]
    name = input('What is your name?')
    name = [c for c in name.lower() if c in 'abcdefghijklmnopqrstuvwxyz']
    puzzle = []
    pos = 0
    for c in name:
        word = choice([*filter(lambda w:c in w, words)])
        marker = choice([i for i, w in enumerate(word) if w == c])
        word = word[:marker] + c.upper() + word[marker+1:]
        puzzle += [[word, marker]]
        pos = max(pos, marker)
    for word, marker in puzzle:
        print(' '*(pos-marker)+word)
