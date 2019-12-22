# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from model import data_manager


sales_list = data_manager.get_table_from_file('sales/sales.csv')
sales_file = 'sales/sales.csv'

list_labels = ['id: ', 'Employee ID: ', 'Customer ID: ', 'Product ID: ', 'Number of items: ']

temp = [""]
    

def run():
    options = ["Print list",
               "Add record",
               "Update record",
               "Remove record",
               'Transaction by employee',
               'Transaction by customer']

    

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice('SALES MENU', options)
        if choice == "1":       # show list of all records
            terminal_view.print_table(sales_list, 'Sales list')
        elif choice == "2":     # add record     
            crm.create(sales_list, terminal_view.get_inputs(list_labels, 'Enter transaction data below:', ''), sales_file)
        elif choice == "3":     # update record
            crm.update(sales_list, terminal_view.get_inputs(temp, 'Enter transaction ID to update: ', ''), terminal_view.get_inputs(list_labels[1:], 'Enter id, name or e-mail to update', sales_file), sales_file) 
        elif choice == "4":     # remove record
            crm.delete(sales_list, terminal_view.get_inputs(temp, 'Enter transaction ID to remove: ', ''), sales_file)
        elif choice == '5':
            terminal_view.print_result(crm.read(sales_list, terminal_view.get_inputs(temp, 'ID:', '')), '')
        elif choice == '6':
            terminal_view.print_result(crm.read(sales_list, terminal_view.get_inputs(temp, 'ID:', '')), '')
            crm.delete(sales_list, terminal_view.get_inputs(temp, 'Enter transaction ID to remove: ', ''), sales_file)
        else:
            terminal_view.print_error_message("There is no such choice.")

