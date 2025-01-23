from utils import ReadCSVDataMixin


class Contact(ReadCSVDataMixin):
    """
    A class for representing a contact.

    contacts (list): A list of contacts in the system.

    Attributes:
        first_name (str): The first name of the contact.
        last_name (str): The last name of the contact.
        phone_number (str): The phone number of the contact.
        messages (list): A list of messages related to the contact.

    """
    contacts = []

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name

        # Add leading zero to phone number if it is not already present
        if isinstance(phone_number, int):
            phone_number = f'0{phone_number}'

        self.phone_number = phone_number
        self.messages = []

        # Check if the contact is already in the contacts list
        if self not in Contact.contacts:
            Contact.contacts.append(self)

    def get_messages(self) -> list["Message"]:
        """
        Returns the list of messages related to the contact.
        :return: list of messages related to the contact
        """
        return self.messages
