import child as ch  # Import the child module containing the Child class definition


def load_children(file_path="child.csv"):
  """
  Loads children data from a CSV file into a list of Child objects.

  Parameters:
      file_path (str): Path to the CSV file containing child records.

  Returns:
      list: List of initialized Child objects.
  """
  child_list = []  # Initialize an empty list to store Child objects

  # Open the CSV file safely using a context manager
  with open(file_path) as f:
    # Read file lines and strip trailing newline characters (\n)
    children = f.read().splitlines()

    # Loop through each line in the file
    for line in children:
      # Skip empty lines or header lines if present
      if line.strip() and not line.startswith("child_id"):
        # Split comma-separated values into a list of string fields
        data = line.split(",")

        # Instantiate a Child object (child_id, age_group, fee, guardian_name)
        child = ch.Child(data[0], data[1], float(data[2]), data[3])

        # Append the new Child object to child_list
        child_list.append(child)

  return child_list  # Return the populated list of Child objects


def save_children(child_list, file_path="child.csv"):
  """
  Saves the updated list of Child objects back to a CSV file.

  Parameters:
      child_list (list): List of Child objects to save.
      file_path (str): Destination file path for saving data.
  """
  # Open the file in write mode ('w') to overwrite previous file content
  with open(file_path, "w") as f:
    # Loop through each Child object in the list
    for child in child_list:
      # Format child attributes into a comma-separated CSV line with a newline
      line = (
          f"{child.get_child_id()},{child.get_age_group()},{child.get_fee()},{child.get_guardian_name()}\n"
      )
      # Write the formatted line to the CSV file
      f.write(line)


def find_child_index(child_list, child_id):
  """
  Finds the index position of a child in child_list given their child ID.

  Parameters:
      child_list (list): List of Child objects.
      child_id (str): Target child ID to search for.

  Returns:
      int: List index position if found, or -1 if not found.
  """
  index = 0  # Counter variable tracking current index position
  found_index = -1  # Default output value indicating child ID was not found

  # Loop through each Child object in the list
  for child in child_list:
    # Check if current child's ID matches the requested target ID
    if child.get_child_id() == child_id:
      found_index = index  # Record the current index position
      break  # Exit loop immediately once match is found
    index += 1  # Move counter to the next list position

  return found_index  # Return found index integer or -1


def add_child(child_list):
  """
  Prompts user for child details, validates inputs, and appends a new Child object.

  Parameters:
      child_list (list): Current list of Child objects.

  Returns:
      list: Updated list of Child objects.
  """
  child_id_input = input("Enter child ID: ").upper()  # Prompt user to enter child ID (Non case-sensitive)

  # Check if child ID is unique (not already present in list)
  if find_child_index(child_list, child_id_input) == -1:
    # Define list of valid age groups allowed by the daycare system
    valid_age_group = ["Toddler", "Preschool", "School Age"]
    age_group_input = input(
        "Enter age group: "
    )  # Prompt user to enter age group

    # Validate if entered age group is in the allowed list
    if age_group_input in valid_age_group:
      fee_input = float(
          input("Enter daily fee: ")
      )  # Prompt user for daily fee and convert to float

      # Validate that daily fee is greater than 0
      if fee_input > 0:
        # Create new Child object (guardian_name defaults to empty string)
        new_child = ch.Child(child_id_input, age_group_input, fee_input)
        # Append newly created Child object to main list
        child_list.append(new_child)
        print("Child added.")  # Display success confirmation message
      else:
        print(
            "Fee must be greater than 0."
        )  # Error message for non-positive fee
    else:
      print(
          f"Age group must be one of {valid_age_group}"
      )  # Error message for invalid age group
  else:
    print("Child already exists.")  # Error message for non-unique child ID

  return child_list  # Return the updated child_list


def remove_child(child_list):
  """
  Removes a child record from child_list using their child ID.

  Parameters:
      child_list (list): Current list of Child objects.

  Returns:
      list: Updated list of Child objects.
  """
  child_id_input = input(
      "Enter child ID to remove: "
  ).upper()  # Prompt user for child ID (Non case-sensitive) to remove

  # Find child's index position using find_child_index helper
  index = find_child_index(child_list, child_id_input)

  # Check if child ID was found in the list
  if index != -1:
    child_list.pop(index)  # Remove object at found index position
    print("Child removed.")  # Display success confirmation message
  else:
    print("Child not found.")  # Error message if child ID does not exist

  return child_list  # Return the updated child_list


def check_in_child(child_list):
  """
  Checks in a child by setting guardian name if child exists and is not checked in.

  Parameters:
      child_list (list): Current list of Child objects.

  Returns:
      list: Updated list of Child objects.
  """
  child_id_input = input("Enter child ID: ").upper()  # Prompt user for child ID (Non case-sensitive)
  index = find_child_index(
      child_list, child_id_input
  )  # Search for child index
  guardian_name_input = input(
      "Enter guardian name: "
  )  # Prompt user for guardian name

  # Validate that guardian name is not empty
  if guardian_name_input != "":
    # Check if child ID exists in list
    if index != -1:
      target_child = child_list[index]  # Retrieve Child object at index position

      # Check if child is currently NOT checked in
      if target_child.is_present() == False:
        target_child.check_in(
            guardian_name_input
        )  # Assign guardian name to child
        print("Child checked in.")  # Display success confirmation message
      else:
        print(
            "Child is already checked in."
        )  # Error message if already checked in
    else:
      print("Child not found.")  # Error message if child ID does not exist
  else:
    print(
        "Invalid input. Please enter valid values."
    )  # Error message for blank guardian name

  return child_list  # Return the updated child_list


def check_out_child(child_list):
  """
  Checks out a child by resetting guardian name if child exists and is checked in.

  Parameters:
      child_list (list): Current list of Child objects.

  Returns:
      list: Updated list of Child objects.
  """
  child_id_input = input("Enter child ID: ").upper()  # Prompt user for child ID (Non case-sensitive)
  index = find_child_index(
      child_list, child_id_input
  )  # Search for child index

  # Check if child ID exists in list
  if index != -1:
    target_child = child_list[index]  # Retrieve Child object at index position

    # Check if child is currently checked in
    if target_child.is_present() == True:
      target_child.check_out()  # Reset guardian name to empty string
      print("Child checked out.")  # Display success confirmation message
    else:
      print(
          "Child is already not checked in."
      )  # Error message if child is not checked in
  else:
    print("Child not found.")  # Error message if child ID does not exist

  return child_list  # Return the updated child_list


def view_all_children(child_list):
  """
  Displays all children records and overall attendance summary counts.

  Parameters:
      child_list (list): Current list of Child objects.
  """
  print("\nAll Children")  # Print section title header with a leading newline

  # Check if child_list contains records
  if child_list != []:
    # Loop through list and print each child using Child.__str__()
    for child in child_list:
      print(child)

    total_children_count = len(child_list)  # Count total child records
    checked_in_children_count = 0  # Initialize checked in counter

    # Loop through list to count checked in children
    for child in child_list:
      if child.is_present():
        checked_in_children_count += 1  # Increment counter if present

    # Calculate count of children not checked in
    not_checked_in_children_count = (
        total_children_count - checked_in_children_count
    )

    # Display summary header with 50-character width
    print("\n" + "=" * 50)
    print(f'{"SUMMARY":^50s}')  # Center string "SUMMARY" in 50 character width
    print("=" * 50)

    # Print summary breakdown counts
    print(f"Total Children: {total_children_count}")
    print(f"Checked In: {checked_in_children_count}")
    print(f"Not Checked In: {not_checked_in_children_count}")
  else:
    print(
        "No children records available."
    )  # Output message if child_list is empty


def main_menu():
  """
  Displays main menu options and validates numeric choice input.

  Returns:
      int: Validated selection integer between 1 and 6.
  """
  # Dictionary mapping menu numbers to descriptive text
  main_menu_dict = {
      1: "Add Child",
      2: "Remove Child",
      3: "Check In Child",
      4: "Check Out Child",
      5: "View All Children",
      6: "Exit",
  }

  user_selection = -1  # Initialize selection variable to invalid default value
  print()  # Print leading newline before displaying menu options

  # Loop repeatedly until a valid choice (1 through 6) is entered
  while user_selection < 1 or user_selection > 6:
    # Print each menu option line
    for key, value in main_menu_dict.items():
      print(f"{key}) {value}")

    user_input = input("Select option: ")  # Get menu option input from user

    # Ensure input string consists only of digits before converting to int
    if user_input.isdigit():
      user_selection = int(user_input)  # Convert numeric string to integer

    # Display error message if entered choice is outside valid range
    if user_selection < 1 or user_selection > 6:
      print("Invalid option.\n")

  return user_selection  # Return validated menu choice integer


def main():
  """
  Entry point for YYC Daycare System.

  Coordinates data loading, menu options, and saving.
  """
  print()  # Print opening blank line
  print("*" * 50)  # Print 50-character border line
  print(f'{"Welcome to YYC Daycare System":^50s}')  # Print centered title banner
  print("*" * 50)  # Print 50-character border line

  child_list = load_children()  # Load child records from CSV file at startup
  print(f"{len(child_list)} child records loaded")  # Print loaded count message

  user_selection = 0  # Initialize variable to track menu selection

  # Program main loop continues until user selects option 6 (Exit)
  while user_selection != 6:
    user_selection = main_menu()  # Call main_menu to prompt and receive choice

    # Use match/case structure to route user menu selection
    match user_selection:
      case 1:
        add_child(child_list)  # Add new child record
      case 2:
        remove_child(child_list)  # Remove child record
      case 3:
        check_in_child(child_list)  # Check in child
      case 4:
        check_out_child(child_list)  # Check out child
      case 5:
        view_all_children(child_list)  # View all children and summary
      case 6:
        save_children(child_list)  # Save list to file on exit
        print("Data saved. Goodbye.\n")  # Display farewell message


# Boilerplate check ensuring main() runs when file is executed directly
if __name__ == "__main__":
  main()