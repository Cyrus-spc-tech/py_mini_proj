import getpass

username = getpass.getuser()
prompt = f"Enter your password ({username}): "
password = getpass.getpass(prompt)

print("You entered:", password)