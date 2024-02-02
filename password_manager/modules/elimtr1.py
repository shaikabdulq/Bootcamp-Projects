# Eliminate using easy Criteria
from modules.elimtr2 import *
cdict = {}

# Function to identify if letter is Upper/Lower/Spl Char/Digit
def letter_type(letter):
    if letter == " ":
        return "whitespace"
    elif letter in list_data['lwr_alpts']:
        return index_list_data[0]
    elif letter in list_data['upr_alpts']:
        return index_list_data[1]
    elif letter in list_data['sp_char']:
        return index_list_data[3]
    else:
        return index_list_data[2]

# Function to check if the letters of password has a particular letter_type
def check_letters(password, parm):
    for i in password:
        if letter_type(i) == parm:
            return True
    return False

# Function to check if the range is matching the criteria
def check_range(password):
    if 8 <= len(password) <= 32:
        return True

# Function to check for whitespaces
def check_space(password):
    if check_letters(password, 'whitespace'):
        return False
    else:
        return True
