import os

# Get the current working directory
current_dir = os.getcwd()

# Define a new directory name
new_dir = os.path.join(current_dir, "new_directory")

# Create the new directory
os.mkdir(new_dir)
print(f"Directory '{new_dir}' created successfully.")

os.chdir(new_dir)
print(f"Directory changed to '{new_dir}'.")
text=os.path.join(new_dir, "text.md")
f=open(text, "w")
f.write("# Text File \n This is a text file created using Python os module .")

# Delete the new directory
# os.rmdir(new_dir)
# print(f"Directory '{new_dir}' deleted successfully.")