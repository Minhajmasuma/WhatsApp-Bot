# WhatsApp-Bot
This project implements a WhatsApp bot using Python, allowing users to automate message sending, receive commands, and respond accordingly. The bot uses the pywhatkit library for sending WhatsApp messages at specified times and the speech_recognition library for voice command recognition. It provides a structured way to handle incoming commands and interact with users on WhatsApp.

Commands Used in Command Prompt
Installation Commands:
Clone the repository:

bash

git clone https://github.com/your_username/whatsapp-bot.git
cd whatsapp-bot
Install required libraries:


pip install pywhatkit
pip install SpeechRecognition
pip install pyttsx3
Running the Bot:
Run the bot script:
Copy code
python whatsapp_bot.py
Follow the on-screen instructions to interact with the bot.
Libraries Used in Python
pywhatkit

Purpose: Used for sending WhatsApp messages programmatically.
Installation: pip install pywhatkit
Documentation: PyPI - pywhatkit
SpeechRecognition

Purpose: Used for recognizing speech input from the user.
Installation: pip install SpeechRecognition
Documentation: PyPI - SpeechRecognition
pyttsx3

Purpose: Used for text-to-speech conversion, enabling the bot to speak responses.
Installation: pip install pyttsx3
Documentation: PyPI - pyttsx3
Project Structure
whatsapp_bot.py: Main script implementing the WhatsApp bot functionality.

Features
Message Sending: Automate sending WhatsApp messages at specified times.
Voice Command Recognition: Recognize voice commands using SpeechRecognition for interaction.
Text-to-Speech: Utilize pyttsx3 to enable the bot to speak responses.
Example Usage
Sending a Scheduled Message:

Input the recipient's number, message, hour, and minute to schedule a WhatsApp message.
Voice Command Interaction:

Initiate interaction with the bot by speaking a command like "Hello" to start the bot.
Conclusion
This WhatsApp bot project provides a practical example of automating messaging and interacting via WhatsApp using Python. It leverages several libraries to achieve functionality such as scheduled messaging and voice command recognition, enhancing user interaction and automation capabilities. The GitHub repository includes installation instructions, usage guidelines, and code documentation to facilitate easy deployment and customization.
