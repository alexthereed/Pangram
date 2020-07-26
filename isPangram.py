#regular expressions module will be utilized to 'clean' string
import re


def isPangram(s):
    '''
    Function to check if a given string is a pangram

    A pangram is a string that contains every letter of the alphabet at least once
    '''
    #remove punctuation and special characters using regular expressions and make sure all remaining letters are lower case
    clean_string = re.sub('[^A-Za-z]+','',s).lower()
    #turning cleaned string into a set to remove repeated letters
    set_string = set(clean_string)

    #if set is 26 items in length then the string is a pangram
    if len(set_string) == 26:
        return 'This string is a pangram'
    #if set contains any other number of items in length then it is not a pangram and will print out the number of unique characters that the string contains
    else:
        return f'This string only contains {len(set_string)} unique letters of the alphabet, it is not a pangram'




