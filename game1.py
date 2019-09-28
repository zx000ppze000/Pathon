# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 11:14:01 2018

@author: zhangx
"""

import random
import math
VOWELS = 'aeiou'      
NONVOWELS = 'bcdfghjklmnpqrstvwxyz' 
HAND_SIZE = int(input('Enter total number of hands: ')) # how many letters does user want in the hand              
                                           
SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
# set all letter values

Word_list = "words_1.txt"
"""load_words function"""
def load_words():

    inFile = open(Word_list, 'r')           # open the file and read each line of the file to give it a list
    wordList = []                               
    for line in inFile:                         
        wordList.append(line.strip().lower())   # add all element to dictionary in a lower case
    print ("  ", len(wordList), "words loaded.") 
    return wordList                             

"""get_word_score function"""
def get_word_score(word, n):
    
    s_element1 = 0     # first element of the scroe calculation
    for letter in word:
        s_element1 += SCRABBLE_LETTER_VALUES[letter]     # add all values of letter that been inputed from the dictionary to calculate first element
    s_element2 = 7 * len(word) - 3 * (n - len(word))     # second element (given by instractor)
    if s_element2 < 1:   # because it has to be greater than 1 so we give it a value if the score below one
        s_element2 = 1
    total_score = s_element1 * s_element2
    return total_score     # return the final score

"""get_frequency_dict function"""
def get_frequency_dict(combnation):
   
    freqency = {}                                   # make freqency to be a dictionary 
    for i in combnation:
        freqency[i] = freqency.get(i,0) + 1         # get each letter and make it to be 1 when it only show up, if it shows up twice
                                                    # it will be assigned 1 at first time and it will add 1 each time
    return freqency
	
"""display_hand function"""
def display_hand(hand):
    
    for letter in hand.keys():     # screen each letter(keys) in the dictionary
        for i in range(hand[letter]):    #  print the letter of hand dictionary keys every loop
            print(letter,end = "")     # print in one line

"""deal_hand function"""
def deal_hand(n):

    hand={}   # assisgn an empty dictionary to hand 
    nov = math.floor(n / 3)  # base on the requirment the number of vowels should be n/3 and it should be integer
    hand.update({'*':1})    # add * to hand dictionary
    SCRABBLE_LETTER_VALUES.update({'*':1}) # update the * Scrabble_letter_values dictionary to be 1
    for i in range(0, nov-1, 1):  # for vowels count and screen the letter key every time with increment 1
        x = random.choice(VOWELS) # random choose the letter from vowels for n/3 times
        hand[x] = hand.get(x, 0) + 1
    for j in range(nov, n, 1):    
        y = random.choice(NONVOWELS)  # random choose the letter from nonvowels for 2n/3 times
        hand[y] = hand.get(y, 0) + 1
    return hand
#
# 以上不用改了
    
"""update_hand function"""
def update_hand(hand, word):

    newhand = hand.copy()  #copy hand to newhand, but if hand changed, newhand will not change
    for letter in word:
        if newhand.get(letter,0) > 0:  #if letter exists(>0),value of this letter should minus 1;
            newhand[letter] -= 1
        elif newhand.get(letter, -1) == 0:  #if letter not exists(==0),set it to default value -1,and delete it.
            del(newhand[letter])
    return newhand

#
"""is_valid_word function"""
def is_valid_word(word, hand, word_list):

    words = []
    match = False # initial the flag
    w_list = list(word) #set a list of the word that been inputed and use lower case
    if '*' in w_list:  # if there is a "*" in the list
        index_num = w_list.index('*')  # set a index number to it (get a position of *)
        for letter in VOWELS:   # check the vowels catagry
            w_list[index_num] = letter  # assign the * index to letter that in word we input every time to match in the word list
            words.append("".join(w_list))  #add every element to the word list with *
    else:
        words.append(word)   # add every element to the word list witought *
    for w in words:  # Searches all posible words in word_list
        if w in word_list:  # if the word is in the list
            match = True   # set flag to be true
    if not match:   #if there is no match in the word list set flag to be false
        return False 
    # The word is entirely composed of letters in the hand
    word_freq_dict = get_frequency_dict(word) #give word_frequency_dict the value of function get_frequency_dict
    for letter, freqency in word_freq_dict.items():  #check every keys and values of word_frequency_dict(letter,freq)
        if freqency > hand.get(letter, 0):   #if freq > the items in letter means they are not exactly the same, return false
            return False  
    return True  #else return true
    

"""play_hand function"""
def play_hand(hand, word_list):

    total = 0
    letters = 0  
    for key, value in hand.items():  # search each in dictionary of hand
        letters += value    # calculate the hand length (number of letters)
# 以下需要改
    while letters > 0:
        print("Current Hand:", end= " ")
        display_hand(hand)
        word = input("Please enter a word or '!!' to indicate you are done: ")
        if word == '!!':
            break
        else:
            if is_valid_word(word, hand, word_list):
                wordscore = get_word_score(word, letters)
                total += wordscore
                print('"' + word + '"', "earned", wordscore, "points. Total:", total, "points")
            else:
                print("That is not a valid word. Please choose another word.")
            hand = update_hand(hand, word)
    if letters == 0:
        print("Ran out of letters.", end=' ')
    print("Total score for this hand:", total, "points")
    print("_____________________________________")
    return total


"""substitute_hand function"""
def substitute_hand(hand, letter):

    newletter1 = False
    ALL_ALPH = VOWELS + NONVOWELS
    if letter not in hand:
        return hand
    while not newletter1:
        newletter = random.choice(ALL_ALPH)
        if newletter not in hand:
            newletter1 = True
            newhand = dict()
            for key, value in hand.items():
                if key == letter:
                    newhand[newletter] = value
                else:
                    newhand[key] = value
                
    return newhand       
    
"""game_main function"""
def game_main(word_list):

    sub_flag = False    # pre set the flag to be false
    replay_flag = False
    finalscore = 0      # initialise the value for finalscore
    for n in range(HAND_SIZE):   # get all letters from deal_hand function and set it to hand every time when the number of input 
        hand = deal_hand(HAND_SIZE)  # reaches the hand size that we inputed 
        if not sub_flag:  # if the flag is not false
            print("Current Hand:", end= " ")  # show the current hand
            display_hand(hand)  # run display_hand function
            substitute = input('Would you like to substitute a letter? ')  # ask user if they want a substitute
            if substitute == 'yes':  # if the user input yes 
                sub_flag = True   # set the flag to be ture so it won't run substitde again and when we reset the game it will goes in the loop
                letter = input('Which letter would you like to replace: ')  # ask user do they want which letter would they replace
                hand = substitute_hand(hand, letter)  # run substitude_hand
        handscore = play_hand(hand, word_list) # calculate the hand score
        if not replay_flag:  # if the flag is not false
            replay = input('Would you like to replay the hand? ')  # ask user to replay the game
            if replay == 'yes':  #  if user input yes 
                replay_flag = True  # set the flag to be ture o it won't run substitde again and when we reset the game it will goes in the loop
                newhand_score = play_hand(hand, word_list)  #  run reset the score from old hand
                if newhand_score > handscore:  #  if the new game get more score than the old one
                    handscore = newhand_score  # replace handscore with new game score
        finalscore += handscore # add the score each time for each time enter a word
    print("Total score over all hands:", finalscore)  # show the final score
    

if __name__ == '__main__':
    word_list = load_words()
    game_main(word_list)