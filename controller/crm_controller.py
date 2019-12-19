# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from model import data_manager

def run():
    options = ["Print list",
               "Add record",
               "Update record",
               "Remove record",
               "Back"]
    
    file_list = "./model/crm/customers.csv"
    list_labels = ['id: ', 'name (first name, last name): ', 'e-mail: ', 'birthdate (yyy-mm-dd): ', 'subscribed (0-no, 1-yes): ']
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
        else:
            terminal_view.print_error_message("There is no such choice.")

    
