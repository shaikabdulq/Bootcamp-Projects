import random
from modules.list import list_data, index_list_data

# Function to generate a random letter
def rdm_letter():
    rdm_list = random.choice(index_list_data)
    letter = random.choice(list_data[rdm_list])
    return letter

# Function to generate a random range (8-32)
def rdm_range():
    lst = list(range(8, 33))
    return random.choice(lst)

# Function to Generate Random password (8-32 long)
def rdm_pass():
    passw = ''
    for i in range(rdm_range()):
        passw += str(rdm_letter())
    return passw
