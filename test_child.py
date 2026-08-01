#
# test_child - This program tests the majority of the methods in the Child class
#
# Author:
# Version/Date:
#
import child as ch

def main():
    # Create a list of 5 children with different age groups
    child_list = []
    
    # Add children with different configurations
    child_list.append(ch.Child("C101", "Preschool", 40.0, "John Smith"))
    child_list.append(ch.Child("C102", "School Age", 35.0, "Maria Garcia"))
    child_list.append(ch.Child("C103", "School Age", 35.0, ""))  # Not checked in
    child_list.append(ch.Child("C104", "Toddler", 50.0, "Robert Johnson"))
    child_list.append(ch.Child("C105", "Preschool", 45.0, ""))  # Not checked in

    # Test getters
    print("Testing getters:")
    current_child = child_list[0]
    print(f"Child ID: {current_child.get_child_id()}")
    print(f"Age Group: {current_child.get_age_group()}")
    print(f"Fee: {current_child.get_fee()}")
    print(f"Guardian Name: {current_child.get_guardian_name()}")
    print()

    # Test is_present() method
    print("Testing is_present():")
    for i in range(len(child_list)):
        if child_list[i].is_present():
            print(f"Child {child_list[i].get_child_id()} is checked in by {child_list[i].get_guardian_name()}")
        else:
            print(f"Child {child_list[i].get_child_id()} is not checked in")
    print()

    # Test check_in() method on a child not checked in
    print("Testing check_in():")
    found = False
    index = 0

    while index < len(child_list) and not found:
        if not child_list[index].is_present():
            found = True
            print(f"Found child not checked in: {child_list[index].get_child_id()}")

            # Check in child
            child_list[index].check_in("Alice Wonderland")
            print(f"After check-in: {child_list[index].get_guardian_name()}")

        index += 1

    if not found:
        print("No available child found for check-in test")
    print()

    # Test check_out() method on a checked-in child
    print("Testing check_out():")
    found = False
    index = 0

    while index < len(child_list) and not found:
        if child_list[index].is_present() and child_list[index].get_guardian_name() != "Alice Wonderland":
            found = True
            print(f"Found checked-in child: {child_list[index].get_child_id()} checked in by {child_list[index].get_guardian_name()}")

            # Check out child
            child_list[index].check_out()
            print(f"After check-out, is present: {child_list[index].is_present()}")

        index += 1

    if not found:
        print("No checked-in child found for check-out test (excluding the one we just checked in)")
    print()

    # Test setters
    print("Testing setters:")
    current_child = child_list[1]  # C102
    print(f"Before - ID: {current_child.get_child_id()}, Age Group: {current_child.get_age_group()}, Fee: {current_child.get_fee()}")

    current_child.set_child_id("C202")
    current_child.set_age_group("Toddler")
    current_child.set_fee(55.0)
    current_child.set_guardian_name("New Guardian")

    print(f"After - ID: {current_child.get_child_id()}, Age Group: {current_child.get_age_group()}, Fee: {current_child.get_fee()}, Guardian: {current_child.get_guardian_name()}")
    print()

    # Print all children using __str__ method
    print("All children (using __str__ method):")
    print("-" * 50)
    for child in child_list:
        print(child)
    print("-" * 50)

    # Summary statistics
    present_count = 0
    for child in child_list:
        if child.is_present():
            present_count += 1

    print("\nSummary:")
    print(f"Total children: {len(child_list)}")
    print(f"Checked in: {present_count}")
    print(f"Not checked in: {len(child_list) - present_count}")


if __name__ == "__main__":
    main()
