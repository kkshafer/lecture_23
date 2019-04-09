import random


def num_vowels(word):
    vowels = 'aeiou'
    num = 0
    for x in word:
        if x in vowels:
            num += 1
    return num



print(num_vowels("woooord"))
