# Imports the Child class from the Child.py File as a short form "ch"
import child as ch

def load_children(file_path="child.csv"):
    """Loads data from csv file into a list of child objects"""

    # Initialize empty child list
    child_list = [] 

    # opens the csv file 
    with open(file_path) as file:

        # reads lines and strips newline characters
        child = file.read().splitlines()

        # loops through lines in file
        for line in child:
            
            if line.strip and not line.startswith("child_id"):

                # splits csv into list of strings
                info = line.split(",")

                # creates the child objects
                kid = ch.Child(info[0], info[1], float(info[2]), info[3])

                # adds the child objects to the child_list
                child_list.append(kid)

    # returnes a list of child objects
    return child_list

    

def save_children(child_list, file_path="child.csv" ):
    """rewrites the csv file with the updates list of children objects"""

    # opens the file in write mode, overwritting previous data
    with open(file_path, "w") as file:

        # Loops through each child object and writes it as a formatted csv line
        for child in child_list:
            line = (f'{child.get_child_id()},{child.get_age_group()},{child.get_fee()},{child.get_guardian_name()}\n')
            file.write(line)       

    # Closes file to avoid data corruption or data leak
    file.close()


def find_child_index(child_list, child_id):

    # initialize veriable
    index = 0

    # inialize variable and default if child not found
    child_index = -1

    # loop through list of child objects looking at the id, and stoping if there is a match
    for child in child_list:
        if child.get_child_id() == child_id:
            child_index = index
            break
        index += 1

    # returning the index number 
    return child_index
        



def add_child(child_list):
    pass

def remove_child(child_list):
    pass

def check_in_child(child_list):
    pass

def check_out_child(child_list):
    pass

def view_all_children(child_list):
    """Displays a formatted menu of all children"""

    # Title printed on new line
    print('\nAll Children')

    # checks for empty list and prints each child object in a formatted string if available

    if child_list != []:
        for child in child_list:
            print(child)
    else:
        print("No children records available")

    # Counts number of children
    total_children = len(child_list)

    # initalizes how many children are checked in
    num_checked_in = 0

    # loops though children and Increments variable if the child is checked in
    for child in child_list:
        if child.is_present():
            num_checked_in += 1

    # Simple math to get the difference between total and num of checked in children
    num_not_checked_in = (total_children - num_checked_in)

    # Prints formatted summery and title
    print(f"="*40)
    print(f"{"SUMMERY":^40s}")
    print(f"="*40)
    print(f"Total Children: {total_children}")
    print(f"Checked In: {num_checked_in}")
    print(f"Not Checked In: {num_not_checked_in}\n")


def main_menu():
    """Main menu display user selection validation"""

    # loops until a valid input is selected
    main_menu_dict = {
        1: "Add Child",
        2: "Remove Child",
        3: "Check In Child",
        4: "Check Out Child",
        5: "View All Children",
        6: "Exit",
    }

    # intial invalid selection to start the loop
    selection = 0  

    # main body of selection look
    while selection < 1 or selection > 6:

        # formats and prints the menu display
        for key, value, in main_menu_dict.items():
            print(f'{key}) {value}')

        # recieves user input
        user_input = input('Select option: ')

        # validates user input as a digit then converts to integer
        if user_input.isdigit():
            selection = int(user_input)

        #  Displays if user inputs an invalid selection
        if selection < 1 or selection > 6:
            print("invalid option. \n")

    # returns the valid selection as an integer
    return selection
        

# Main function that will run on program start
def main():
    """Program entry point for initialization and menu handling"""

    # prints main menu welcome banner
    print('\n' + '*'*40)
    print(f"{"Welcome to YYC Daycare System":^40s}")
    print("*"*40)


    # prints number children info currently in the system 
    child_list = load_children()
    print(f"{len(child_list)} child records loaded.\n")

    # initial invalid choice to start loop 
    selection = 0 

    # will continue to loop until 6 is input
    while selection != 6:

        # funtion call
        selection = main_menu()

        # match case for user navigation with each case matching to a specific function of the program
        match selection:
            case 1:
                add_child(child_list)
            case 2:
                remove_child(child_list)
            case 3:
                check_in_child(child_list)
            case 4:
                check_out_child(child_list)
            case 5:
                view_all_children(child_list)

                # ends the program and saves the info as a csv 
            case 6:
                save_children(child_list)
                print("Data saved. Goodbye. \n")



# Checks if file is run directly by python, if so it will exicute the main function to start the application. 
if __name__ == "__main__":
    main()