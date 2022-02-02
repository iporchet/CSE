# Write a program that reads a character, then reads in a list of words. 
# The output of the program is every word in the list that contains the character at least once. 
# Assume at least one word in the list will contain the given character.

def contains_character(user_input, letter):
    list_of_words = [x for x in user_input.split(' ')]
    
    for x in list_of_words:
        if letter in x:
            print(x)
    

if __name__ == '__main__':
    letter_to_find = str(input())
    user_phrase = str(input())

    contains_character(user_phrase, letter_to_find)