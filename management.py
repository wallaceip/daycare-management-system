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

def save_children(file_path, child_list):
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
    child_id_list = [child.get_child_id() for child in child_list]
    child_id_input = input('Enter child ID: ')
    if child_id_input not in child_id_list:
        
        valid_age_group = ['Toddler', 'Preschool', 'School Age']
        age_group_input = input('Enter age group: ')
        if age_group_input in valid_age_group:
            
            fee_input = int(input('Enter daily fee: '))
            if fee_input >= 0:
                new_child = ch.Child(child_id_input, age_group_input, fee_input)
                print('Child added.')
                return child_list.append(new_child)
            else:
                print('Fee must be greater than 0.')
        else:
            print(f'Age group must be one of {valid_age_group}')
    else:
        print('Child already exists.')
  

def remove_child(child_list):
    ''''''
    child_id_list = [child.get_child_id() for child in child_list]
    child_id_input = input('Enter child ID to remove: ')
    if child_id_input not in child_id_list:
        print('Child not found.')
    if 

def check_in_child(child_list):
    ''''''
    pass

def check_out_child(child_list):
    ''''''
    pass

def view_all_children(child_list):
    ''''''
    pass

def main():
    ''''''
    pass


print("Testing getters:")

child_list = load_children()
for i in range(len(child_list)):
    current_child = load_children('child.csv')[i]
    print(f"Child ID: {current_child.get_child_id()}")
    print(f"Age Group: {current_child.get_age_group()}")
    print(f"Fee: {current_child.get_fee()}")
    print(f"Guardian Name: {current_child.get_guardian_name()}")
    print()