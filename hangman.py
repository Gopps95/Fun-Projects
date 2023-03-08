import json
import random
import string 


f = open('words.json')
data = json.load(f)

def get_valid_word(data):
    while '-' in word or ' ' in word:
        word = random.choice(data)

    return word.upper()


def hangman():
    word = get_valid_word(data)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input('Guess a letter:').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('You have already used the character.')
    else:
        print('Invalid')


user_input = input("Type Something")
