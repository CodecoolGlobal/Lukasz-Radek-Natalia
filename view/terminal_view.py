""" Terminal view module """


def print_table(table, title_list):
    print('-'* 124)
    for line in table:
        print('|', line[0].ljust(8," "), '|', line[1].ljust(40," "), '|',
         line[2].ljust(38," "), '|', line[3].ljust(10," "), '|', line[4].ljust(12," "), '|' )
        print('-'* 124)


def print_result(result, label):
    print('The respult of', label, 'is', result)
  

def print_menu(title, list_options, exit_message):
  print(title)
  i = 0
  for line in list_options:
    i = i+1
    print(i, line)


def get_inputs(list_labels, title):
    print(title)
    answers = []
    for line in list_labels:
        answers.append(input(line))
    return answers


def get_choice(options):
    print_menu("Main menu",options, "Exit program")
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]


def print_error_message(message):
    print('Error:', message)

    
