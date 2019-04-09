import random
import json


def num_vowels(word):
    vowels = 'aeiou' ## defines vowels
    num = 0 ## initializes number of vowels
    for x in word: ## for each letter in the input word
        if x in vowels: ## if the letter is a vowel
            num += 1 ## sum vowels
    return num ## return number of vowels
