# Assignment 2, hangman.py
# Group No/Name: Group 6
# Members: Tao Xu, Xu Zhang, and Ziqi Yang

# Hangman Game
# -----------------------------------
# Helper code

import random
import string
import sys

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



# -------------------------------------
# Hangman Part 1: Three helper functions

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE
    # Initialize counter i
    i = 0
    # Initialize length counter
    len_counter = 0
    # Start a search on each letter in secret word
    while i <= (len(secret_word)-1):
        # Reset counter j
        j = 0
        # Start a search on each letter in letters_guessed
        while j <= (len(secret_word)-1):
            # If the letter matches, length counter increases by 1
            if letters_guessed[j] == secret_word[i]:
                len_counter = len_counter + 1
            # Move to next letter in letters_guessed
            j = j + 1
        # Move to next letter in secret word
        i = i + 1
    # If the length matches, it means the word has been guessed
    if len_counter == len(secret_word):
        # Then return True
        return True
    # Otherwise, return False, which means the word has not been guessed yet
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE
    # Create an array with blanks (" _ ") and its number matches the length of secret word
    guess = [' _ '] * len(secret_word)
    # Initialize counter i
    i = 0
    # Start a search on each letter in letters_guessed
    while i <= (len(letters_guessed)-1):
        # Reset counter j
        j = 0
        # Start a search on each letter in letters_guessed
        while j <= (len(secret_word)-1):
            # If the letter matches
            if secret_word[j] == letters_guessed[i]:
                # Replace the corresponding blank (" _ ") in guess
                guess[j] = letters_guessed[i]
            # Move to next letter in secret word
            j = j + 1
        # Move to next letter in letters_guessed
        i = i + 1
    # Return the result of guessed word
    # Use join() to concentrate the elements in guess
    return ''.join(guess)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE
    # Initialize an alphabet list
    letters_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # Initialize counter i
    i = 0
    # Start a search on each letter in letters_guessed
    while i <= (len(letters_guessed)-1):
        # If the letter in letters_guessed is in the alphabet list
        if letters_guessed[i] in letters_list:
            # Remove it from alphabet list
            letters_list.remove(letters_guessed[i])
        # Move to next letter in letters_guessed
        i = i + 1
    # Return the updated alphabet list
    return ''.join(letters_list)
    
# end of part 1
    

    
    
# -------------------------------------
# Hangman Part 2: The Game

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE
    # Get the length of the secret word and convert it into a string
    length = len(secret_word)
    # Set the guess chance remaining to 6 times
    guesses_remaining = 6
    # Set the warning chance remaining to 3 times
    warning_remaining = 3
    # Set the input letters to an empty array
    letters_guessed = []
    # Set the guess status to false so it can run in the function below first 
    word_guessed = False
    # Obtain the number of unique letters in secret word
    # set() is used here to remove duplicated letter
    unique_letters = len(set(secret_word))
    
    # Game welcome
    print('Welcome to the game, Hangman!')
    # Use the string value we setup before and tell players the length of secret word
    print('I am thinking of a word that is ' + str(length) + ' letters long.')
    print('------------')

    # The player has mistake chances that are not greater than 6 and not less than 0,
    # or the guess status should be false
    while (guesses_remaining > 0 and guesses_remaining <= 6) or word_guessed is False:
        # When the player guessed the correct word, changing the guess status to true so the player knows they win
        if secret_word == get_guessed_word(secret_word, letters_guessed):
            word_guessed = True
            break
        # Notice the player how many guess chance remaining they still have
        print('You have ' + str(guesses_remaining) + ' guesses left.')
        print('------------')
        # Show the player what words that are still available to player
        print('Available letters: ' + str(get_available_letters(letters_guessed)))
        print('------------')
        # Input the letter in lowercase
        guess = input('Please guess a letter: ').lower()
        # Make sure the input letter is a lowercase letter from 'a' to 'z'
        if guess >= 'a' and guess <= 'z':
            # When the letter input is in the secret word
            if guess in secret_word:
                # Add the letter to the empty array and save the position
                letters_guessed.append(guess)
                print('------------')
                print('Good guess: ' + str(get_guessed_word(secret_word, letters_guessed)))
                print('------------')
            # When the letter input is not in the secret word
            else:
                # Add this letter into letters_guessed array
                letters_guessed.append(guess)
                # When the player guesses the letter that is vowel
                if guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess == 'u':
                    # Take two guess chances away
                    guesses_remaining = guesses_remaining - 2
                # When the letter is not a vowel
                else:
                    # Just take one guess away
                    guesses_remaining = guesses_remaining - 1
                print('Oops! That letter is not in my word: ' + str(get_guessed_word(secret_word, letters_guessed)))
                print('------------')
        # When the player inputs a letter that is not in range of lowercase 'a' to 'z'
        else:
            # Check the number of warning is still greater than 0
            if warning_remaining > 0:
                # Take player a warning chance away
                warning_remaining = warning_remaining - 1
                print('Oops! That is not a valid letter. you have ' + str(warning_remaining) + ' left')
                print('------------')
            # If player uses up all the warning chances, guess chances will start losing
            else:
                guesses_remaining = guesses_remaining - 1
        # If the player uses up all the guess chances
        if guesses_remaining == 0:
            # Output "sorry" and tell player what the secret word is
            print('Sorry, you ran out of guesses. The word was "' + secret_word + '".')
            # Then exit the game
            exit(1)
    # If the player guess the right word, tell the player "You win"
    if word_guessed == True:
        print('Congratulations, you win!')
        # Calculate the total score which the player got and output it
        score = guesses_remaining * unique_letters
        print('Your total score for this game is: ', score)
        # Then exit the game
        exit(1)

# -----------------------------------
# end of part 2
    
    
    
# -------------------------------------
# Hangman Part 3: The Game with Hints


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE
    # Initialize counter i
    i = 0
    # Initialize the number of matching
    match_num = 0
    # Initialize the match status to False
    match_flag = False
    # Remove the spaces in my_word by using replace()
    my_word_no_spaces = my_word.replace(' ', '')
    # Make sure the length of my_word without spaces is same as the English word to match
    if len(other_word) == len(my_word_no_spaces):
        # If the length is the same, it will start checking the gaps by looping
        while i <= len(my_word_no_spaces) - 1:
            # If the words matched or it is a '_'
            if my_word_no_spaces[i] == other_word[i] or my_word_no_spaces[i] == '_':
                # Increase the number of matching by 1
                match_num = match_num + 1
                # When the number of matching is same as the length of the English word
                if match_num == len(other_word):
                    # Change the match status to True and break the loop
                    match_flag = True
                    break
            # Move to the next letter
            i = i + 1
    # Return the match status
    return match_flag
  

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE
    # Set array of possible wordlists to empty 
    possible_wordlists = []
    # Initialize counter i
    i = 0
    # Search every word in "word.txt" from the beginning
    while i <= len(wordlist) - 1:
        # Call function match_with_gaps() and check the match status
        if match_with_gaps(my_word, wordlist[i]):
            # Add matched word to possible_wordlists with a space at the end
            possible_wordlists.append(wordlist[i] + ' ')
        # Move to the next word in "word.txt"
        i = i + 1
    # If there is no matched word found
    if len(possible_wordlists) == 0:
        # Output "No possiable matches found"
        print ("No possiable matches found")
        print('------------')
    # If there are matched words found
    else:
        # Output all matched words
        print('All possible matches:')
        # Use join() to concentrate the elements in possible_wordlists
        print(''.join(possible_wordlists))
        print('------------')




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE
    # Get the length of the secret word and convert it into a string
    length = len(secret_word)
    # Set the guess chance remaining to 6 times
    guesses_remaining = 6
    # Set the warning chance remaining to 3 times
    warning_remaining = 3
    # Set the input letters to an empty array
    letters_guessed = []
    # Set the guess status to false so it can run in the function below first 
    word_guessed = False
    # Obtain the number of unique letters in secret word
    # set() is used here to remove duplicated letter
    unique_letters = len(set(secret_word))
    
    # Game welcome
    print('Welcome to the game, Hangman!')
    # Use the string value we setup before and tell players the length of secret word
    print('I am thinking of a word that is ' + str(length) + ' letters long.')
    print('------------')

    # The player has mistake chances that are not greater than 6 and not less than 0,
    # or the guess status should be false
    while (guesses_remaining > 0 and guesses_remaining <= 6) or word_guessed is False:
        # When the player guessed the correct word, changing the guess status to true so the player knows they win
        if secret_word == get_guessed_word(secret_word, letters_guessed):
            word_guessed = True
            break
        # Notice the player how many guess chance remaining they still have
        print('You have ' + str(guesses_remaining) + ' guesses left.')
        print('------------')
        # Show the player what words that are still available to player
        print('Available letters: ' + str(get_available_letters(letters_guessed)))
        print('------------')
        # Input the letter in lowercase
        guess = input('Please guess a letter: ').lower()
        # When the player enters '*', giving a hint of all possible words
        if guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        # Make sure the input letter is a lowercase letter from 'a' to 'z'
        if guess >= 'a' and guess <= 'z':
            # When the letter input is in the secret word
            if guess in secret_word:
                # Add the letter to the empty array and save the position
                letters_guessed.append(guess)
                print('------------')
                print('Good guess: ' + str(get_guessed_word(secret_word, letters_guessed)))
                print('------------')
            # When the letter input is not in the secret word
            else:
                # Add this letter into letters_guessed array
                letters_guessed.append(guess)
                # When the player guesses the letter that is vowel
                if guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess == 'u':
                    # Take two guess chances away
                    guesses_remaining = guesses_remaining - 2
                # When the letter is not a vowel
                else:
                    # Just take one guess away
                    guesses_remaining = guesses_remaining - 1
                print('Oops! That letter is not in my word: ' + str(get_guessed_word(secret_word, letters_guessed)))
                print('------------')
        # When the player inputs a letter that is not in range of lowercase 'a' to 'z', except '*'
        elif guess != '*':
            # Check the number of warning is still greater than 0
            if warning_remaining > 0:
                # Take player a warning chance away
                warning_remaining = warning_remaining - 1
                print('Oops! That is not a valid letter. you have ' + str(warning_remaining) + ' left')
                print('------------')
            # If player uses up all the warning chances, guess chances will start losing
            else:
                guesses_remaining = guesses_remaining - 1
        # If the player uses up all the guess chances
        if guesses_remaining <= 0:
            # Output "sorry" and tell player what the secret word is
            print('Sorry, you ran out of guesses. The word was "' + secret_word + '".')
            # Then exit the game
            quit()
    # If the player guess the right word, tell the player "You win"
    if word_guessed == True:
        print('Congratulations, you win!')
        # Calculate the total score which the player got and output it
        score = guesses_remaining * unique_letters
        print('Your total score for this game is: ', score)
        # Then exit the game
        quit()

# -----------------------------------
# end of part 3

# Main code 

# To test part 2
# uncomment the following two lines.
    
# secret_word = choose_word(wordlist)
# hangman(secret_word)


    
# To test part 3 re-comment out the above lines and 
# uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)