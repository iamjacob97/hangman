import random
from wordbank import words
import string

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left and used the letters {','.join(used_letters)}")
        guessed_word = [letter if letter in used_letters else '-' for letter in word]
        print(f"The word is {' '.join(guessed_word)}")
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print("You have already used this letter.")
        else:
            print("You have input an invalid character.")
    if lives == 0:
        print(f"Sorry, You have died. The word was {word}.")
    else:
        print(f"You guessed the word {word} !!")

hangman()
    

