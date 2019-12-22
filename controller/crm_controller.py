# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from model import data_manager

def run():
    options = ["Print list",
               "Add record",
               "Update record",
               "Remove record",
               'Find by ID/name/e-mail',
               "What is the id of the customer with the longest name?",
               "Which customers have subscribed to the newsletter?",
               'Get youngest customer',
               'Get age by..']
    
    file_list = "./model/crm/customers.csv"
    list_labels = ['id: ', 'name (first name, last name): ', 'e-mail: ', 'birthdate (yyyy-mm-dd): ', 'subscribed (0-no, 1-yes): ']
    remove = ['']

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice('CRM MENU', options)
        if choice == "1":
            terminal_view.print_table(data_manager.get_table_from_file(file_list), 'CRM list')
        elif choice == "2":
            crm.create(data_manager.get_table_from_file(file_list), terminal_view.get_inputs(list_labels, 'Enter personal data here:', file_list), file_list)
        elif choice == "3":
            crm.update(data_manager.get_table_from_file(file_list), terminal_view.get_inputs(remove, 'Enter id, name or e-mail to update: ', ''), terminal_view.get_inputs(list_labels[1:], 'Enter id, name or e-mail to remove',file_list), file_list)
        elif choice == "4":
            crm.delete(data_manager.get_table_from_file(file_list), terminal_view.get_inputs(remove, 'Enter id, name or e-mail to remove: ', ''), file_list)
        elif choice == "5":
            terminal_view.print_table(crm.read(data_manager.get_table_from_file(file_list), terminal_view.get_inputs(remove, 'Enter id, name or e-mail to find: ', '')),'The record is')
        elif choice == "6":
            terminal_view.print_table(crm.get_longest_name_id(data_manager.get_table_from_file(file_list)), "Customer with the longest name:")
        elif choice == "7":
            terminal_view.print_table(crm.get_subscribed_emails(data_manager.get_table_from_file(file_list)), "List of customers subscribed to newsletter:")
        elif choice == "8":
            terminal_view.print_table(crm.get_youngest_customer(data_manager.get_table_from_file(file_list)), '')
        elif choice == "9":
            terminal_view.print_table(crm.get_age_by(terminal_view.get_inputs(remove, 'Enter id, name or e-mail to get age: ', ''), data_manager.get_table_from_file(file_list), terminal_view.get_inputs(remove, 'Enter the current year: ', '')), 'The age is: ')
        else:
            terminal_view.print_error_message("There is no such choice.")



