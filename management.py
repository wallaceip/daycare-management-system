import child as ch

def load_children(file_path='child.csv'):
    '''Loads children data from a CSV file into a list of objects.'''

    child_list = []
    with open(file_path) as f:
        # Read file contents and split into individual lines, stripping newlines (\n)
        children = f.read().splitlines()
        
        # Loop through each line in the file
        for line in children:
            # Split comma-separated string into a list of data attributes
            data = line.split(',')

            # Instantiate a new Child object passing the parsed attribute fields
            child = ch.Child(data[0], data[1], data[2], data[3])
            
            # Add the newly created Child object to the main list
            child_list.append(child)

    return child_list

def save_children(child_list, file_path='child.csv'):
    '''Save the updated list of Child objects back to a CSV file.'''

    with open(file_path, 'w') as f:
        for child in child_list:
            line = f"{child.get_child_id()},{child.get_age_group()},{child.get_fee()},{child.get_guardian_name()}\n"
            f.write(line)


def find_child_index(child_list, child_id):
    '''Find the index of the child provided the child id, returns -1 if not found.'''

    index = 0
    found_index = -1 # Default value if not found

    for child in child_list:
        if child.get_child_id() == child_id:
            found_index = index
        index += 1

    return found_index

def add_child(child_list):
    ''''''
    child_id_input = input('Enter child ID: ')
    
    # Use find_child_index instead of creating child_id_list
    if find_child_index(child_list, child_id_input) == -1:
        
        valid_age_group = ['Toddler', 'Preschool', 'School Age']
        age_group_input = input('Enter age group: ')

        if age_group_input in valid_age_group:
            fee_input = int(input('Enter daily fee: '))

            if fee_input >= 0:
                new_child = ch.Child(child_id_input, age_group_input, fee_input)
                child_list.append(new_child)
                print('Child added.')

                return child_list

            else:
                print('Fee must be greater than 0.')
        else:
            print(f'Age group must be one of {valid_age_group}')
    else:
        print('Child already exists.')
  

def remove_child(child_list):
    '''Removes a child from the list of children using their child ID.'''
    child_id_input = input('Enter child ID to remove: ')
    
    # Get the index of the child (-1 if not found)
    index = find_child_index(child_list, child_id_input)
    
    if index != -1:
        child_list.pop(index)  # pop() removes the item at the specified index position
        print('Child removed.')

        return child_list
    else:
        print('Child not found.')

def check_in_child(child_list):
    child_id_input = input('Enter child ID: ')
    index = find_child_index(child_list, child_id_input)
    guardian_name_input = input('Enter guardian name: ')
    if guardian_name_input != "":
        if index != -1:
            target_child = child_list[index]
            if target_child.is_present() == False:
                target_child.check_in(guardian_name_input)
                print('Child checked in.')

                return child_list
            
            else:
                print('Child is already checked in.')
        else:
            print('Child not found.')
    else:
        print('Invalid input. Please enter valid values.')

def check_out_child(child_list):
    ''''''
    child_id_input = input('Enter child ID: ')
    index = find_child_index(child_list, child_id_input)
    if index != -1:
        target_child = child_list[index]
        if target_child.is_present() == True:
            target_child.check_out()
            print('Child checked out.')

            return child_list
        
        else:
            print('Child is already not checked in.')

    else:
        print('Child not found.')

def view_all_children(child_list):
    ''''''
    print('\nAll Children')
    if child_list != []:
        for child in child_list:
            print(child)

        total_children_count = len(child_list)
        checked_in_children_count = 0
        for child in child_list:
            if child.is_present():
                checked_in_children_count += 1

        not_checked_in_children_count = total_children_count - checked_in_children_count

        print('\n'+'='* 50)
        print(f'{'SUMMARY':^50s}')
        print('='* 50)
        print(f'Total Children: {total_children_count}')
        print(f'Checked In: {checked_in_children_count}')
        print(f'Not Checked In: {not_checked_in_children_count}')

        return
    else:
        print('No children records available.')

def main_menu():
    """Displays menu options and validates user selection input."""
    main_menu_dict = {
        1: 'Add Child',
        2: 'Remove Child',
        3: 'Check In Child',
        4: 'Check Out Child',
        5: 'View All Children',
        6: 'Exit'
    }

    # Loop prompts user repeatedly until valid choice (1-5) is entered
    user_selection = -1
    print()
    while user_selection < 1 or user_selection > 5:
        for key, value in main_menu_dict.items():
            print(f'{key}) {value}')

        user_input = input('Select option: ')
        # Ensure user entered a number before attempting integer conversion
        if user_input.isdigit():
            user_selection = int(user_input)

        if user_selection < 1 or user_selection > 5:
            print('Invalid option. Please try again.\n')

    return user_selection 

def main():
    ''''''
    print()
    print('*'* 50)
    print(f'{'Welcome to YYC Daycare System':^50s}')
    print('*'* 50)
    child_list = load_children()
    print(f'{len(child_list)} child records loaded')
    user_selection = 0
    while user_selection != 5:
        user_selection = main_menu()
        match user_selection:
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
            case 6:
                save_children(child_list)
                print('Data saved. Goodbye.')

    
# Check if this file is being run directly by Python (rather than imported into another script)
# If running directly, execute the main() function to start the application
if __name__ == "__main__":
    main()

