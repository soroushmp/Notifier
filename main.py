import tkinter as tk
from tkinter import filedialog

from contacts import Contact
from messages import Message
from settings import SMS_SERVICE

# Ask user to select a file
# ========================
# tkinter basic gui
root = tk.Tk()
root.withdraw()
# ask user to select a file
file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
# ========================

# Main Codes
# ========================


# Make Contacts in Bulk From CSV File
contacts = Contact.convert_csv_to_bulk_instance(file_path)

# Get Default Message Text
text = input('Enter Message Text: ')

# Make Messages From Contacts And Text
messages = [Message(text=text, contact=contact) for contact in contacts]

# Send Messages Using SMS Service (Kavenegar) one by one
results = map(SMS_SERVICE.send_sms, messages)

# Print Results Status
for result in results:
    print(f"Contact Name: {result.contact.first_name} {result.contact.last_name}")
    print(f"Phone Number: {result.contact.phone_number}")
    print('-' * 20)
    print(f"Message Text: {result.text}")
    print('-' * 20)
    print(f"Status: {result.status}")
    print(f"Response: {result.response}")
    print('=' * 50, end='\n\n')
