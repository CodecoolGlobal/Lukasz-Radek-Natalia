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
def create(table, record):
    table.append(record)
    return table


"""
    Get the record from the table by id

    Args:
        table (list): table to get from the record
        id_ (str): id of the record

    Returns:
        list: record
"""
def read(table, id_):
    for line in table:
        if id_ in line:
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
def update(table, id_, record):
    for line in table:
        if id_ in line:
            line[1:] = record
        else:
            pass
    return record    



"""
    Removes a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
"""
def delete(table, id_):
    for line in table:
        if id_ in line:
            table.remove(line)
        else:
            pass
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

    pass


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
    pass


def get_age_by(surname, table):
    pass


def get_email_by(surname, table):
    pass


def get_first_name_by(surname, table):
    pass
