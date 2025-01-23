# Educational Project for Python OOP Course

This project is designed as a practical tool to help students understand and apply Object-Oriented Programming (OOP) concepts in Python. It involves managing contacts, sending SMS messages, and integrating with an external SMS service (Kavenegar). The project provides hands-on experience in working with classes, attributes, methods, and real-world data handling.

## Project Structure

```
.
├── contacts
│   └── models
│       └── contact.py
├── integration
│   └── models
│       ├── kavenegar_sms_service.py
│       └── sms_service_abstract.py
├── messages
│   └── models
│       └── message.py
├── settings.py
├── utils.py
└── main.py
```

### Key Components

1. **`contacts.models.contact`**: Defines the `Contact` class, which represents a contact with attributes such as `first_name`, `last_name`, and `phone_number`. It also includes a mixin for bulk creation from CSV files.

2. **`integration.models.kavenegar_sms_service`**: Implements the `KavenegarSMSService` class to handle SMS sending using the Kavenegar API.

3. **`integration.models.sms_service_abstract`**: Provides an abstract base class (`SMSService`) for SMS services, defining the structure for sending single and bulk messages.

4. **`messages.models.message`**: Defines the `Message` class, which links contacts with messages, tracks message status, and updates status based on API responses.

5. **`settings.py`**: Configures environment variables and initializes the SMS service instance.

6. **`utils.py`**: Contains the `ReadCSVDataMixin` for converting CSV data into instances of the subclass.

7. **`main.py`**: The entry point of the application, where contacts are loaded from a CSV file, messages are created, and SMS messages are sent using the Kavenegar API.

## Requirements

- Python 3.11+
- Virtual environment
- Required Python libraries listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/soroushmp/Notifier.git
   cd <repository-folder>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file to store environment variables:
   ```
   KAVENEGAR_API_KEY=<Your-API-Key>
   KAVENEGAR_MAIN_URL=https://api.kavenegar.com
   KAVENEGAR_API_VERSION=v1
   KAVENEGAR_SEND_SMS_ENDPOINT=sms/send.json
   OVERWRITE_MESSAGE_TEXT=True
   ```

## How to Run the Project

1. Run the `main.py` file:
   ```bash
   python main.py
   ```

2. Follow the prompts:
   - Select a CSV file containing contact data.
   - Enter the default message text.

3. The application will:
   - Load contacts from the selected CSV file.
   - Create messages for each contact.
   - Send SMS messages using the Kavenegar API.
   - Print the results for each message.

### CSV File Format
The CSV file should contain the following columns:

| first_name | last_name | phone_number |
|------------|-----------|--------------|
| John       | Doe       | 09121234567  |
| Jane       | Smith     | 09309876543  |

### Example Output

```
Enter Message Text: this is a test message.
Contact Name: John Doe
Phone Number: 09121234567
--------------------
Message Text: Hello John Doe
this is a test message.
--------------------
Status: sent
Response: <Response [200]>
==================================================

Contact Name: Jane Smith
Phone Number: 09309876543
--------------------
Message Text: Hello Dear User
this is a test message.
--------------------
Status: failed
Response: <Response [412]>
==================================================
```

## Notes

- Ensure the `.env` file is correctly configured with valid Kavenegar API credentials.
- The project currently does not implement bulk SMS sending.
- Error handling for failed requests is minimal and can be expanded for robustness.

Feel free to reach out with any questions or suggestions for improvement!

