# Imports the Child class from the Child.py File as a short form "ch"
import child as ch

def load_children(file_path):
    pass

def save_children(file_path, child_list):
    pass

def find_child_index(child_list, child_id):
    pass

def add_child(child_list):
    pass

def remove_child(child_list):
    pass

def check_in_child(child_list):
    pass

def check_out_child(child_list):
    pass

def view_all_children(child_list):
    pass

def main_menu():
    """Main menu display user selection validation"""
    main_menu_dict = {
        1: "Add Child",
        2: "Remove Child",
        3: "Check In Child",
        4: "Check Out Child",
        5: "View All Children",
        6: "Exit",
    }

    selection = 0

    while selection < 1 or selection > 6:
        for key, value, in main_menu_dict.items():
            print(f'{key}) {value}')

        user_input = input('Select option')
        if user_input.isdigit():
            selection = int(user_input)
        if selection < 1 or selection > 6:
            print("invalid option: \n")
    return selection
        

# Main function that will run on program start
def main():
    """Program entry point for initialization and menu handling"""
    print('\n' + '*'*40)
    print(f"{"Welcome to YYC Daycare System":^40s}")
    print("*"*40)

    selection = 0 
    while selection != 6:
        selection = main_menu()

        match selection:
            case 1:
                add_child(child_list)
            case 2:
                remove_child(child_lsit)
            case 3:
                check_in_child(child_list)
            case 4:
                check_out_child(child_list)
            case 5:
                view_all_children(child_list)
            case 6:
                save_children(child_list)
                print("Data saved. Goodbye. \n")



# Checks if file is run directly by python, if so it will exicute the main function to start the application. 
if __name__ == "__main__":
    main()