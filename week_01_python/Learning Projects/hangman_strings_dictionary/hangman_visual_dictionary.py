import random
from words import words #imports variable list words (2nd) from words.py file (1st)
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words): #some words contain spaces or dashes and can not be recognized
    word = random.choice(words) #randomly chooses word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word, set() converts word to iterable elements with distinct elements, called Set
    alphabet = set(string.ascii_uppercase) #converts letters to upper case
    used_letters = set() #what the user has guessed
    
    lives = 7
    
    #getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have ', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        
        # what current word is (ex, W - RD)
        word_list = [letter if letter in used_letters else '-' for letter in word] #create a list with letters which are used in word
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                lives = lives - 1 #takes away a life if letter is guessed wrong
                print('\nYour letter,', user_letter, 'is not in word.')
                
        elif user_letter in used_letters:
            print('\nYou have already used that character. Please try again.')
            
        else:
            print('\nInvalid character. Please try again.')
            
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You lost, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!!')
        
hangman()

