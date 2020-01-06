# everything you'll need is imported:
from model.store import store
from view import terminal_view
from model import data_manager
import os


def run():
    terminal_view.clear()
    options = ["Print list",
               "Add record",
               "Update record",
               "Remove record",
               "Get counts by manufacturers",
               "Get averege by manufacturer",
               "Get oldest game",
               "Get chepest game",
               "Get age by", 
               "Get game by"]
    
    file_list = "./model/store/games.csv"
    list_labels = ['id: ', 'title: ', 'manufacturer: ', 'price: ', 'release_date (yyyy-mm-dd): ']
    remove = ['']
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice('GAMES MENU', options)
        terminal_view.clear()
        if choice == "1":
            terminal_view.print_table(data_manager.get_table_from_file(file_list), 'GAMES list')
        elif choice == "2":
            store.create(data_manager.get_table_from_file(file_list), terminal_view.get_inputs(list_labels, 'Enter personal data here:', file_list), file_list)
        elif choice == "3":
            store.update(data_manager.get_table_from_file(file_list), terminal_view.get_inputs(remove, 'Enter id, name or e-mail to update: ', ''), terminal_view.get_inputs(list_labels[1:], 'Enter id, name or e-mail to remove',file_list), file_list)
        elif choice == "4":
            store.delete(data_manager.get_table_from_file(file_list), terminal_view.get_inputs(remove, 'Enter id, name or e-mail to remove: ', ''), file_list)
        elif choice == "5":
            terminal_view.print_table(store.get_counts_by_manufacturers(data_manager.get_table_from_file(file_list)),'The record is')
        elif choice == "6":
           terminal_view.print_result(store.get_average_by_manufacturer(data_manager.get_table_from_file(file_list), terminal_view.get_inputs(remove, 'Enter the game title', '')), 'Average by manufacturer: ')
        elif choice == "7":
            terminal_view.print_result(store.get_oldest_game(data_manager.get_table_from_file(file_list)), 'Get the oldest game')
        elif choice == "8":
            terminal_view.print_result(store.get_cheapest_game(data_manager.get_table_from_file(file_list)), 'Get the the cheapest game')
        elif choice == "9":
            terminal_view.print_result(store.get_age_by(terminal_view.get_inputs(remove, 'Enter the game title', ''), data_manager.get_table_from_file(file_list), terminal_view.get_inputs(remove, 'Enter the current year: ', '')), 'The age is: ')
        elif choice == "10":
            terminal_view.print_table(store.get_game_by(terminal_view.get_inputs(remove, 'Enter the game title', ''), data_manager.get_table_from_file(file_list)), 'The game is/are: ')
        else:
            terminal_view.print_error_message("There is no such choice.")


