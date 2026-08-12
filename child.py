class Child:
    '''A class to represent a child in the daycare system'''

    # Initialize private attributes (__ prefix enforces encapsulation)
    def __init__(self, child_id, age_group, fee, guardian_name=""): # guardian_name is set to empty by default (not checked in)
        self.__child_id = child_id
        self.__age_group = age_group
        self.__fee = fee
        self.__guardian_name = guardian_name  # Empty string signifies 'Not Checked In'

    # --- Getters ---
    def get_child_id(self):
        return self.__child_id

    def get_age_group(self):
        return self.__age_group

    def get_fee(self):
        return self.__fee

    def get_guardian_name(self):
        return self.__guardian_name

    # --- Setters ---
    def set_child_id(self, child_id):
        self.__child_id = child_id
    
    def set_age_group(self, age_group):
        self.__age_group = age_group

    def set_fee(self, fee):
        self.__fee = fee

    def set_guardian_name(self, guardian_name):
        self.__guardian_name = guardian_name

    # --- Attendance Operations ---
    def is_present(self):
        # Presence is derived directly from whether a guardian is registered
        return self.__guardian_name != ""

    def check_in(self, guardian_name):
        self.__guardian_name = guardian_name

    def check_out(self):
        self.__guardian_name = ""  # Clearing guardian marks child as checked out

    # Returns formatted output string when object is printed or converted to str
    def __str__(self):
        # Non-empty guardian_name indicates child is actively checked in
        if self.__guardian_name != "":
            # Format includes child metadata and active guardian name
            return f'Child {self.__child_id} | {self.__age_group} | Fee: {float(self.__fee):.1f} | Checked In by {self.__guardian_name}'
        # Empty guardian_name indicates child is not currently present
        else:
            # Format displays standard 'Not Checked In' status flag
            return f'Child {self.__child_id} | {self.__age_group} | Fee: {float(self.__fee):.1f} | Not Checked In'