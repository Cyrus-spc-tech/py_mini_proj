import pywhatkit as kit

# Define the phone number and message
phone_number = "+91 7006623705"  # Replace with the recipient's phone number
message = "Hello, this is an automated message from Python!"
hour = 13  # 24-hour format
minute = 36  # The minute you want to send the message

# Send the message
kit.sendwhatmsg(phone_number, message, hour, minute)