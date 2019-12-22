# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from model import data_manager

temp = ['']

def run():
    options = ["Print list",
               "Add record",
               "Update record",
               "Remove record",
               'Transaction by employee',
               'Transaction by customer']
    
   

    list_labels = ['ID: ', 'Employee name: ', 'Customer name: ', 'Product ID: ', 'Number of items: ']
    sales_list = data_manager.get_table_from_file('sales/sales.csv')
   

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice('SALES MENU', options)
        if choice == "1":       # show list of all records
            terminal_view.print_table(data_manager.get_table_from_file(sales_list), 'CRM list')
        elif choice == "2":     # add record            
            print("tralala")           
        elif choice == "3":     # update record
            print("tralala")    
        elif choice == "4":     # remove record
            print("tralala")    
        elif choice == '5':
            terminal_view.print_result(crm.read(sales_list, terminal_view.get_inputs(temp, 'ID:', '')), '')
        elif choice == '6':
            terminal_view.print_result(crm.read(sales_list, terminal_view.get_inputs(temp, 'ID:', '')), '')
        else:
            terminal_view.print_error_message("There is no such choice.")




    