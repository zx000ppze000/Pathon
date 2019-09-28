# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 21:48:22 2018

@author: M18
"""


import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 9

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words_1.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1 #若存在x，返回x的value为0，+1为计数，不管存在不存在。若不存在则生成一个x，并使其为0，作为初始化。
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.
    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 
	The score for a word is the product of two components:
	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played
	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    score1 = 0
    for letter in word:
        score1 += SCRABBLE_LETTER_VALUES[letter]
    
    score2 = 7 * len(word) - 3 * (n - len(word))
    if score2 < 1:
        score2 = 1
        
    return score1 * score2
    

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.
    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.
    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end =' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).
    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.
    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    numvowels = int(n // 3)

    hand['*'] = 1
    
    for i in range(numvowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(numvowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    newhand = hand.copy()   #copy hand to newhand, but if hand changed, newhand will not change
    word = word.lower()     #convert to lower cases
    
    for letter in word:
        if newhand.get(letter,0) > 0:#if letter exists(>0),value of this letter should minus 1;
            newhand[letter] -= 1 
        
        if newhand.get(letter, -1) == 0: #if letter not exists(==0),set it to default value -1,and delete it.
            del(newhand[letter])
            
    return newhand    #return newhand value

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    words = []   #set words to empty array
    word = word.lower()  #convert to lower cases
    
    
    wordlist = list(word)   #convert word to wordlist
    
 
    if '*' in wordlist:  #if user input *
        pos = wordlist.index('*')  # get the position of *
        for letter in VOWELS:   #
            wordlist[pos] = letter   #replace * with letter
            words.append("".join(wordlist))   #delete the space
    else:
        words.append(word)  #if user hasn`t use *, add the letter in words array
        
        
          
    found = False         # give found initial value and Search all posible words in word_list
    for i in words:
        if i in word_list:
            found = True  #if match, give found true
    
    if not found:        #if not match, give found False
        return False
    
   
    
  
    word_frequency_dict = get_frequency_dict(word)  #give word_frequency_dict the value of function get_frequency_dict
    for letter, freq in word_frequency_dict.items(): #check every keys and values of word_frequency_dict(letter,freq)
        if freq > hand.get(letter, 0):              #if freq > the items in letter means they are not exactly the same, return false
            return False
    
    return True                                  #else return true
    

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    letters = 0
    
    for i in hand.items():
        letters = len(hand)
        
    return letters


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    
    * The user may input a word.
    * When any word is entered (valid or invalid), it uses up letters
      from the hand.
    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    

    total = 0    #initial total to 0

    while calculate_handlen(hand) > 0: #if the hand has not been used up.
        print("Current Hand:", end= " ") #print current in one line
        display_hand(hand)               #call function display_hand
        word = input("Please enter a word or '!!' to indicate you are done: ")#get word
        if word == '!!':     #if user input !!, then break
            break
        else:
            if is_valid_word(word, hand, word_list):#call is valid word 
                wordscore = get_word_score(word, calculate_handlen(hand))#get score using get word score
                total += wordscore #get total score
                print('"' + word + '"', "earned", wordscore, "points. Total:", total, "points")
                
            else:
                print("That is not a valid word. Please choose another word.")
            hand = update_hand(hand, word) #update hand
    if calculate_handlen(hand) == 0:  #if hand is used up, print Ran out of letters.
        print("Ran out of letters.", end=' ') 
    print("Total score for this hand:", total, "points") #show the total value
    print("-"*10)
    return total  


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.
    If user provide a letter not in the hand, the hand should be the same.
    Has no side effects: does not mutate hand.
    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    if letter not in hand:
        return hand
    
    newletter1 = False
    
    while not newletter1:   #while True
        newletter = random.choice(VOWELS + CONSONANTS) #choose random letter in vowels and consonants
        if newletter not in hand: #选择的不在hand里
            newletter1 = True    
            newhand = dict()   #创建dictionary
            for key, value in hand.items():  
                if key == letter:
                    newhand[newletter] = value
                else:
                    newhand[key] = value
                
    return newhand       
    

def play_game(word_list):
    """
    Allow the user to play a series of hands
    * Asks the user to input a total number of hands
    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.
    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.
            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands
    word_list: list of lowercase strings
    """
    
    total_hands = int(input('Enter total number of hands: '))#get user input
    finalscore = 0                                           #initial final score, substitute, replay
    lettersubstitute = False                                 
    handreplay = False
    
    for n in range(total_hands):   #in range of Enter total number of hands:
        hand = deal_hand(HAND_SIZE) #get random hand with value of HAND_SIZE
        if not lettersubstitute:   #user not to substitute
            print("Current Hand:", end= " ") 
            display_hand(hand)
            substitute = input('Would you like to substitute a letter? ')  #function of substitute with adjustment yes or no
            if substitute.lower() == 'yes':  
                lettersubstitute = True
                letter = input('Which letter would you like to replace: ')
                hand = substitute_hand(hand, letter)
        handscore = play_hand(hand, word_list)  #function of calculating score
        if not handreplay:
            replay = input('Would you like to replay the hand? ')# function about replay yes or no
            if replay.lower() == 'yes':
                handreplay = True
                newhand_score = play_hand(hand, word_list) 
                if newhand_score > handscore:
                    handscore = newhand_score
        finalscore += handscore       #get final score and print 
        
    print("Total score over all hands:", finalscore)
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)