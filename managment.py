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

# Main function that will run on program start
def main():
    """Program entry point for initialization and menu handling"""
    print('\n' + '*'*40)
    print(f"{"Welcome to YYC Daycare System":^40s}")
    print("*"*40)



# Checks if file is run directly by python, if so it will exicute the main function to start the application. 
if __name__ == "__main__":
    main()