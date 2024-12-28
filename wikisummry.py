#import the necessary module!
import pywhatkit as kt

#display welcome msg
print('Lets Generate Wiki Summary!\n')

# Get user input for search term
src = input("What You want to search About: ")
# Get user input for number of lines and validate it
while True:
    try:
        line = int(input("How many lines you want to display: "))
        if line > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
kt.info(src,lines=line)
#kt.search(src)