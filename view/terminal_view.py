""" Terminal view module """
from model.crm import crm
from model import data_manager


def print_table(table, title_list):
    print(title_list)
    print('-'* 124)
    if len(table) > 5:
        for line in table:
            print('|', line[0].ljust(8," "), '|', line[1].ljust(40," "), '|',
            line[2].ljust(38," "), '|', line[3].ljust(10," "), '|', line[4].ljust(12," "), '|' )
            print('-'* 124)
    else:
        print('|', table[0].ljust(8," "), '|', table[1].ljust(40," "), '|',
        table[2].ljust(38," "), '|', table[3].ljust(10," "), '|', table[4].ljust(12," "), '|' )
        print('-'* 124)


def print_result(result, label):
    print('The respult of', label, 'is', result)
  

def print_menu(title, list_options, exit_message):
    print(title)
    i = 0
    for line in list_options:
        i = i+1
        print(i, line)
    print('0', exit_message)


def get_inputs(list_labels, title, file_list):
    print(title)
    answers = []
    for line in list_labels:
        if 'id' in line:
            a = (crm.generate_random(data_manager.get_table_from_file(file_list)))
            print('id:', a)
            answers.append(a)
        else:
            a = input(line)
            answers.append(a)
    return answers


def get_choice(menu_name, options):
    print_menu(menu_name,options, "Back/Exit program")
    inputs = get_inputs(["Please enter a number: "], "", "")
    return inputs[0]


def print_error_message(message):
    print('Error:', message)

    
