import pywhatkit as kit
from datetime import datetime

# Getting the current time
now = datetime.now()

# Mobile number input
mobile = input('Enter Mobile No of Receiver (with country code, e.g., +1234567890): ')

# Message input
message = input('Enter the message you want to send: ')

# Time input
hour = int(input('Enter the hour (24-hour format): '))
minute = int(input('Enter the minute: '))

try:
    # Sending the WhatsApp message
    kit.sendwhatmsg(mobile, message, hour, minute)
    print("Message scheduled successfully")
except Exception as e:
    print(f"An error occurred: {e}")
