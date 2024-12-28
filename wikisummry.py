#import the necessary module!
import pywhatkit as kt

#display welcome msg
print('Lets Generate Wiki Summary!\n')

# Get user input for search term
src = input("What You want to search About: ")
line = int(input("How many lines you want to read: "))
kt.info(src,lines=line)
#kt.search(src)