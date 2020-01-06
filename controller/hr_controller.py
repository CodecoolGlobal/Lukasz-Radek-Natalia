# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
from model import data_manager

def run():
    options = ["Print list",
               "Add record",
               "Update record",
               "Remove record",
               'Find by ID/name/e-mail',
               'Who is the oldest employee?',
               'Who has the shortest surname?',
               "Get age by",
               "Get email by",
               "Get first name by"]
    
    file_list = "./model/hr/persons.csv"
    list_labels = ['id: ', 'name (first name, last name): ', 'e-mail: ', 'birthdate (yyyy-mm-dd): ', 'salary: ']
    remove = ['']

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice('HR MENU', options)
        if choice == "1":
            terminal_view.print_table(data_manager.get_table_from_file(file_list), 'HR list')
        elif choice == "2":
            hr.create(data_manager.get_table_from_file(file_list), terminal_view.get_inputs(list_labels, 'Enter personal data here:', file_list), file_list)
        elif choice == "3":
            hr.update(data_manager.get_table_from_file(file_list), terminal_view.get_inputs(remove, 'Enter id, name or e-mail to update: ', ''), terminal_view.get_inputs(list_labels[1:], 'Enter id, name or e-mail to remove',file_list), file_list)
        elif choice == "4":
            hr.delete(data_manager.get_table_from_file(file_list), terminal_view.get_inputs(remove, 'Enter id, name or e-mail to remove: ', ''), file_list)
        elif choice == "5":
            terminal_view.print_result(hr.read(data_manager.get_table_from_file(file_list), terminal_view.get_inputs(remove, 'Enter id, name or e-mail to remove: ', '')),'The record is')
        elif choice == "6":
            terminal_view.print_result(hr.get_oldest_person(data_manager.get_table_from_file(file_list)), "The oldest employee is:")
        elif choice == "7":
            terminal_view.print_result(hr.get_shortest_surname(data_manager.get_table_from_file(file_list)), "Employee with the shortest surname is:")             
        elif choice == "8":
            terminal_view.print_result(hr.get_age_by(terminal_view.get_inputs(remove, 'Enter id, name or e-mail to get age: ', ''), data_manager.get_table_from_file(file_list), terminal_view.get_inputs(remove, 'Enter the current year: ', '')), 'The age is: ')
        elif choice == "9":
            terminal_view.print_result(hr.get_email_by(terminal_view.get_inputs(remove, 'Enter surname: ', ''), data_manager.get_table_from_file(file_list)), '')
        elif choice == "10":
            terminal_view.print_result(hr.get_first_name_by(terminal_view.get_inputs(remove, 'Enter surname: ', ''), data_manager.get_table_from_file(file_list)), '')
        else:
            terminal_view.print_error_message("There is no such choice.")

    