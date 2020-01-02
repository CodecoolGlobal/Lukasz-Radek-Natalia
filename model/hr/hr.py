""" Human resources module"""

# everything you'll need is imported:
import random
from model import data_manager


"""
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
"""
def generate_random(table):
    all_characters = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
     'O', 'P', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z'], 
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z'], 
    ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(' ,')' ,'_', '-',
     '+', '=', '{' , '}' , '}', '|', ':', ',', '"', '<', '>','.','?','/']]
    generated_list = []
    for a in range(len(all_characters)):
        for i in range(2):
            generated_list.append(random.choice(all_characters[0+a]))
    generated = ''.join(generated_list)
    if generated_list in table:
        generate_random(table)
    else:
        pass
    return generated


"""
    Adds new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
"""
def create(table, record, file_name):
    table.append(record)
    data_manager.write_table_to_file(file_name, table)
    return table


"""
    Get the record from the table by id

    Args:
        table (list): table to get from the record
        id_ (str): id of the record

    Returns:
        list: record
"""
def read(table, idl):
    record = []
    id_s = ''.join(idl)
    for line in table:
        if id_s in line:
            record = line
        else:
            pass
    return record




"""
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
"""
def update(table, id_, record, file_name):
    id_s = ''.join(id_)
    for line in table:
        if id_s in line:
            line[1:] = record 
            print('Update OK')          
        else:            
            pass
    data_manager.write_table_to_file(file_name, table)
    return record
   



"""
    Removes a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
"""
def delete(table, id_, file_name):
    for line in table:
        id_s = ''.join(id_)
        if id_s in line:
            table.remove(line)
            print('Remove OK')
        else:
            pass
    data_manager.write_table_to_file(file_name, table)
    return table

# special functions:
# ------------------



def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """


    for oldest_person in range(len(table)-1,0,-1):         
        for i in range(oldest_person):
            if table[i][3][0:4] < table[i+1][3][0:4]:           # compares year
                temp = table[i]
                table[i] = table[i+1]
                table[i+1] = temp
            elif table[i][3][0:4] == table[i+1][3][0:4]:        # if year is the same
                if table[i][3][5:7] < table[i+1][3][5:7]:       # compares month
                    temp = table[i]
                    table[i] = table[i+1]
                    table[i+1] = temp
                elif table[i][3][5:7] == table[i+1][3][5:7]:    # if month is the same
                    if table[i][3][8:] < table[i+1][3][8:]:     # compares day
                        temp = table[i]
                        table[i] = table[i+1]
                        table[i+1] = temp
    return table[i-1]


def get_persons_closest_to_average_salary(table):
    """
    Question: Who is the closest to the average salary?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    pass


def get_shortest_surname(table):
    for shortest_surname in range(len(table)-1,0,-1):
        for i in range(shortest_surname):
            if len(table[i][1].split(" ")[-1]) > len(table[i+1][1].split(" ")[-1]):
                temp = table[i]
                table[i] = table[i+1]
                table[i+1] = temp
    return table[i]


def get_age_by(surname, table, current_year):
    record = []
    record1 = []
    surname_s = ''.join(surname)
    for line in table:
        if surname_s in line:
            record = line[3]
            age = record[0:4]
            age1 = int(''.join(current_year))
            age2 = age1 - int(age)
            record1.append(str(age2))
        else:
            pass
    return record1


def get_email_by(surname, table):
    i = 0
    result = []
    email = []
    surname_s = ''.join(surname)  # the get_inputs function always returns a list, this option may be useful
    for line in table:
        result.append(line[1])
        mylist = [i.split(' ') for i in result]
    for line1 in mylist:
        i = i + 1
        if surname_s in line1:  
            email.append(table[i-1][2])
    return email


def get_first_name_by(surname, table):
    i = 0
    result = []
    first_name = []
    surname = ''.join(surname) 
    for line in table:
        result.append(line[1])
        mylist = [i.split(' ') for i in result]
    for line1 in mylist:
        i = i + 1
        if surname in line1:
            first_name.append(table[i-1][1].split(" ")[0])
    return first_name
