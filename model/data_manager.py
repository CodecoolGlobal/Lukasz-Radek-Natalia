"""
    Reads csv file and returns it as a list of lists.
    Lines are rows columns are separated by ","

    Args:
        file_name (str): name of file to read

    Returns:
         list: List of lists read from a file.
"""


def get_table_from_file(file_name):
    with open(file_name, 'r') as file:
        result = []
        for line in file:
            columns = line.split(',')
            result.append(columns)
    return result


"""
    Writes list of lists into a csv file.

    Args:
        file_name (str): name of file to write to
        table (list): list of lists to write to a file

    Returns:
         None
"""


def write_table_to_file(file_name, table):
    with open(file_name, 'w') as file:
        for line in table:
            file.write(','.join([str(x) for x in line]))           
    return

#get_table_from_file('games.csv')
#write_table_to_file('games2.csv', get_table_from_file('games.csv'))