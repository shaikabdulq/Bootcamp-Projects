# Eliminate using medium Criteria
from modules.list import *


# Function to find keywords from strings (user_id and org.)
def find_keywords(string):
    import re
    pattern = r'[A-Za-z]+|\d+'
    return re.findall(pattern, string)


# Function to check if password contains any item from list
def check_for_keywords(list, password):
    found = False
    for i in list:
        # print(i, type(i))
        if str(i) in password:
            found = True
        # print(found)
    return found


# Must not match with the user_id
def check_userid(user_id, password):
    list = find_keywords(user_id)
    cases_to_list(list)
    if check_for_keywords(list, password):
        return False
    else:
        return True


# Function to add upper, lower and camel cases possibilities to an existing list
def cases_to_list(list):
    new_list = []
    for i in list:
        try:
            lower = i.lower()
            upper = i.upper()
            camel = i.capitalize()
            if lower in list:
                pass
            else:
                new_list.append(lower)
            if upper in list:
                pass
            else:
                new_list.append(upper)
            if camel in list:
                pass
            else:
                new_list.append(camel)
        except:
            continue
    list.extend(new_list)


# Must not use the name of org
def check_org(org, password):
    list = find_keywords(org)
    cases_to_list(list)
    if check_for_keywords(list, password):
        return False
    else:
        return True


# Must not be a commonly used password
def check_dlist(password):
    list = danger_list
    cases_to_list(list)
    if check_for_keywords(list, password):
        return False
    else:
        return True
