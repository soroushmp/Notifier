import requests

import settings
from integration.models.sms_service_abstract import SMSService


class KavenegarSMSService(SMSService):
    """
    Kavenegar SMS Service
    """

    def __init__(self):
        super().__init__()

    def send_sms(self, message: "Message") -> "Message":
        """
        Logic to send Single SMS
        :param message: Message
        :return Response
        """
        url = f"{settings.KAVENEGAR_MAIN_URL}/{settings.KAVENEGAR_API_VERSION}/{settings.KAVENEGAR_API_KEY}/{settings.KAVENEGAR_SEND_SMS_ENDPOINT}?receptor={message.contact.phone_number}&message={message.text}"
        # Send SMS Using Kavenegar API And Get Response
        response = requests.request("GET", url)

        # Update Message Status After Sending
        message.update_status(response)

        # Return Updated Message
        return message

    def send_sms_bulk(self, messages: list["Message"], message_text: str) -> list[requests.Response]:
        # Todo: Implement Send SMS Bulk Method
        raise NotImplementedError('Send bulk SMS using Kavenegar not implemented')
