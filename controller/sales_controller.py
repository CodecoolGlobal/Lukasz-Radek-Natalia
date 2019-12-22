# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from model import data_manager


def run():
    options = ["Print list",
               "Add record",
               "Update record",
               "Remove record",
               'Find by ID/name/e-mail']
    
 file_list = "./model/crm/customers.csv"
    list_labels = ['id: ', 'name (first name, last name): ', 'e-mail: ', 'birthdate (yyyy-mm-dd): ', 'subscribed (0-no, 1-yes): ']
    remove = ['']

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice('SALES MENU', options)
        if choice == "1":
            pass
        elif choice == "2":
           pass
        elif choice == "3":
           pass
        elif choice == "4":
            pass
        elif choice == "5":
          pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        elif choice == "9":
           pass
        else:
            terminal_view.print_error_message("There is no such choice.")


    