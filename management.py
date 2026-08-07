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
    pass

def remove_child(child_list):
    pass

def check_in_child(child_list):
    pass

def check_out_child(child_list):
    pass

def view_all_children(child_list):
    pass

def main():
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