import os
#taking path of file 
fd = "D:\\vscode\\py.work\\asset\\osnewfile.txt"

#checking if file exists
if os.path.exists(fd):
    print("File exists")

# opening the file in write mode
file = open(fd, 'w')

# writing to the file
file.write("Hello this is the new line we have added \n")
file.write("This is the second line we have added ")

# close the file
file.close()

# opening in appending mode
with open(fd, 'a') as file:
    file.write("\nThis is the appended line in the file")
file.close()


# opening again in read mode
file = open(fd, 'r')
text = file.read()
print(text)