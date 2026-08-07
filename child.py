class Child:
    '''A class to represent a child in the daycare system'''

    # Constructor
    def __init__(self, child_id, age_group, fee, guardian_name=""):
        self.__child_id = child_id
        self.__age_group = age_group
        self.__fee = fee
        self.__guardian_name = guardian_name

    # Getters
    def get_child_id(self):
        return self.__child_id

    def get_age_group(self):
        return self.__age_group

    def get_fee(self):
        return self.__fee

    def get_guardian_name(self):
        return self.__guardian_name

    # Setters
    def set_child_id(self, child_id):
        self.__child_id = child_id
    
    def set_age_group(self, age_group):
        self.__age_group = age_group

    def set_fee(self, fee):
        self.__fee = fee

    def set_guardian_name(self, guardian_name):
        self.__guardian_name = guardian_name

    # Check-in boolean
    def is_present(self):
        if self.__guardian_name != "":
            return True
        else:
            return False

    # Check in/ out methods
    def check_in(self, guardian_name):
        self.__guardian_name = guardian_name

    def check_out(self):
        self.__guardian_name = ""


    def __str__(self):
        if self.__guardian_name != "":
            return f'Child {self.__child_id} | {self.__age_group} | Fee: {float(self.__fee):.1f} | Checked In by {self.__guardian_name}'
        else:
            return f'Child {self.__child_id} | {self.__age_group} | Fee: {float(self.__fee):.1f} | Not Checked In' 
        




