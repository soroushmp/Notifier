from datetime import datetime

import requests

import settings
from contacts import Contact


class Message:
    """
    A message sent to a contact, relation between contact and message text
    A Contact can have several Messages related to it
    """
    MESSAGE_STATUS_SENT = "sent"
    MESSAGE_STATUS_FAILED = "failed"
    MESSAGE_STATUS_PENDING = "pending"

    MESSAGE_STATUS_CHOICES = (
        (MESSAGE_STATUS_SENT, "sent"),
        (MESSAGE_STATUS_PENDING, "pending"),
        (MESSAGE_STATUS_FAILED, "failed"),
    )

    def __init__(self, contact: Contact, text: str | None = None):
        self.text = text
        self.contact = contact
        self.created_at = datetime.now()

        # Message Status Attributes For Tracking Status Changes And Time Of Status Change After Send
        self.change_status_datetime = None
        self.status: Message.MESSAGE_STATUS_CHOICES = Message.MESSAGE_STATUS_PENDING

        # SMS Service Response
        self.response: requests.Response | None = None

        if settings.OVERWRITE_MESSAGE_TEXT:
            # Generate and Update Message Text Based On Contact Phone Number
            self._generate_message_text()

        # Add Message To Contact Messages List
        self.contact.messages.append(self)

    def _generate_message_text(self) -> None:
        """
        Generate and Update Message Text Based On Contact Phone Number
        """
        if self.contact.phone_number.startswith('0912'):
            self.text = f"Hello {self.contact.first_name} {self.contact.last_name}\n{self.text}"
        else:
            self.text = f"Hello Dear User\n{self.text}"

    def update_status(self, response: requests.Response) -> None:
        """
        Update Message After Sending Message To Contact Based On Response of SMS Service
        :param response: Response
        """
        self.response = response
        self.change_status_datetime = datetime.now()

        if response.status_code == 200:
            self.status = self.MESSAGE_STATUS_SENT
        else:
            self.status = self.MESSAGE_STATUS_FAILED

    # Magic Methods For String Representation
    def __str__(self) -> str:
        """
        String Representation Of Message Object For Printing
        :return: str
        """
        return f"{self.contact.first_name} {self.contact.last_name} - {self.text} - {self.status}"
