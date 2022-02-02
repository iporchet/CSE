#An acronym is a word formed from the initial letters of words in a set phrase. 
# Write a program whose input is a phrase and whose output is an acronym of the input. 
# Append a period (.) after each letter in the acronym. 
# If a word begins with a lower case letter, don't include that letter in the acronym. 
# Assume the input has at least one upper case letter.

def acronym(strng_input):
    list_of_words = [x for x in strng_input.split(' ')]
    list_of_Letters = [strng_input[x] for x in range(0, len(strng_input)) if strng_input[x].isupper() == True]

    return '.'.join(list_of_Letters)

if __name__ == '__main__':
    
    user_string = str(input())

    print(acronym(user_string))