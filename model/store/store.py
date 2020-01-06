""" Store module """

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

def get_counts_by_manufacturers(table):
    manufacturer = {}
    company_name = []
    result = []
    for line in table:
        manufacturer.update({line[2]: 0})
        company_name.append(line[2])  
    for line in company_name:
        manufacturer[line] = manufacturer[line] + 1
    for key, value in manufacturer.items():
        temp = [key+':'+str(value)]
        result.append(temp)
    return result


def get_average_by_manufacturer(table, manufacturer):
    record1 = 0
    i = 0
    average = ['This is no such game in the stock']
    manufacturer_s = ''.join(manufacturer)
    for line in table:
        if manufacturer_s in line:
            record1 = int(record1) + int(line[3])
            i = i + 1
            average.clear()
            a = record1/i           
            average.append(str(a))
    return average
   

def get_oldest_game(table):
    n = (len(table))
    iterations = 1
    while iterations < n:
        j = 1
        while j <= n-2:
            if table[j][4] < table[j+1][4]:
                temp = table[j+1]
                temp2 = table[j]
                table[j+1] = temp2
                table[j] = temp
                j += 1
            else:
                j += 1
        iterations += 1
        result = table[n-1]
    return result


def get_cheapest_game(table):
    n = (len(table))
    iterations = 1
    while iterations < n:
        j = 1
        while j <= n-2:
            if table[j][3] < table[j+1][3]:
                temp = table[j+1]
                temp2 = table[j]
                table[j+1] = temp2
                table[j] = temp
                j += 1
            else:
                j += 1
        iterations += 1
        result = table[n-1]
    return result


def get_age_by(surname, table, current_year):
    record = []
    record1 = ['This is no such game in the stock']
    surname_s = ''.join(surname)
    for line in table:
        if surname_s in line:
            record = line[4]
            age = record[0:4]
            age1 = int(''.join(current_year))
            age2 = age1 - int(age)
            record1.clear()
            record1.append(str(age2))
    return record1


def get_game_by(keyword, table):
    i = 0
    a = 0
    result = []
    name = []
    keywords_s = ''.join(keyword)
    for line in table:
        result.append(line[1])
        mylist = [i.split(' ') for i in result]
    for line1 in mylist:
        i = i + 1
        if keywords_s in line1:
            name.append(table[i-1])
    return name