# everything you'll need is imported:
from view import terminal_view
from controller import store_controller
from controller import hr_controller
from controller import crm_controller
import os


def run():
    terminal_view.clear()
    options = ["Store manager",
               "Human resources manager",
               "Customer Relationship Management (CRM)",
               "Sales manager"]
    
    choice = None
    while choice != "0":
        terminal_view.clear()
        choice = terminal_view.get_choice('Main menu', options)
        if choice == "1":
            store_controller.run()
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            crm_controller.run()
        elif choice == '4':
            sales_controller.run()
        else:
            terminal_view.print_error_message("There is no such choice.")
