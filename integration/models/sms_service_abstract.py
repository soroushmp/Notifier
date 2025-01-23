from requests import Response


class SMSService:
    """
    Abstract class for SMS service
    """

    def __init__(self):
        pass

    def send_sms(self, message: "Message") -> Response:
        """
        Logic to send Single SMS
        :param message: Message
        """
        pass

    def send_sms_bulk(self, messages: list["Message"], message_text: str) -> list[Response]:
        """
        Logic to send bulk SMS
        :param messages:
        :param message_text:
        """
        pass
