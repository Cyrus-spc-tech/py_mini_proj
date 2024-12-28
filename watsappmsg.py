import pywhatkit as kit

# Define the phone number and message
country_code=input("Enter Country Code: ")
phone=int(input("Enter Phone Number: "))
phone_number = str(country_code)+str(phone)
message=input("Enter Message: ")
hour=int(input("Enter Hour in 24 hour format: "))
minute=int(input("Enter Minute: "))

# Send the message
kit.sendwhatmsg(phone_number, message, hour, minute)