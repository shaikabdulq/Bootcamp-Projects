# 5. Saving org, username and password in file
# Use PrettyTable to save data in file
# Organisation | Username |Password

from prettytable import PrettyTable

# Reads all rows from confidential.txt and returns a list
def read_rows():
    rows=[]
    fhand = open('confidential.txt')
    count = 0
    for i in fhand:
        count += 1
        if count > 3:
            if i.startswith("+"): continue
            else: rows.append(i.rstrip())
    return rows

# Reads all rows from confidential.txt, identifies key-value pairs and returns a list of dicts
def capture_file():
    list_of_dicts =[]
    rows = read_rows()
    for line in rows:
        dict = {'org': None, 'login_id': None, 'passw': None}
        #Remove '|' from the start and end
        line = line[1:-1]
        #print(line)
        list = line.split('|')
        #print(list)
        new_list=[]
        for i in list:
            i = i.strip()
            new_list.append(i)
        #print("new_list",new_list)
        dict['org']= new_list[0]
        dict['login_id'] = (new_list[1])
        dict['passw']=(new_list[2])
        list_of_dicts.append(dict)
    return list_of_dicts

# Creates a pretty table using data (list of dicts) and returns table
def create_ptable(list_of_dicts):
    table = PrettyTable()
    table.field_names = ['Organisation', 'Username','Password']
    for i in range(len(list_of_dicts)):
        table.add_row(list_of_dicts[i].values())
    return table

# Writes the pretty table in file
def write_ptable(list_of_dicts):
    table = create_ptable(list_of_dicts)
    fhand = open('confidential.txt', 'w')
    fhand.write(str(table))
    fhand.close()

# Append to list_of_dicts in new row
def new_row(org, login_id,password,list_of_dicts):
    dict = {'org': org, 'login_id': login_id, "passw": password}
    list_of_dicts.append(dict)
    return list_of_dicts

# Append to list_of_dicts in existing row
def existing_row(org, login_id,password,list_of_dicts):
    list_of_dicts[lookup(org,login_id,list_of_dicts)]['passw'] = password
    return list_of_dicts

# Searches for matching org and user id in existing data and returns its index location
def lookup(org,login_id,list_of_dicts):
    count = 0
    for dict in list_of_dicts:
        if (dict['org'] == org or dict['org'].lower() == org) and dict['login_id'] == login_id:
            return count
        count += 1
