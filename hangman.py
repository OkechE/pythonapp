import random #imports the functions from the random library
from words import words #imports the the words variable from the words.py file
import string

def get_valid_word(words): #defines a function using thev words variable 
    word = random.choice(words) #chooses a random word from the words variable
    while '-'in word or ' ' in word: 
        word = random.choice(words) #continues to choose a random word if a space or dash are chosen
         
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #keeps track of the letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #keeps track of the letters guessed

    user_letter = input('Guess a Letter:').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
             word_letters.remove(user_letter) 

        elif user_letter in used_letters:
            print('Try a different letter')

        else:
            print('invalid letter')


user_input = input('type something:')
print(user_input)
