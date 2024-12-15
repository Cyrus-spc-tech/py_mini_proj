#importing a nessasary module to intract with operrating system in locam machine 
import os 

#use to print current working directory 
curdir=os.getcwd()
print(curdir)
# use to change current working directory
# os.chdir('/home/your_username/your_directory_name')
# use path of the directory you want to change to

# change th name of file by path 
os.rename('D:\\vscode\\py.work\\asset\\osfile.txt', 'D:\\vscode\\py.work\\asset\\osnewfile.txt')
#use '\\' to avoid issues with escape sequences

# OR >>  os.rename(r'D:\vscode\py.work\asset\osfile.txt', r'D:\vscode\py.work\asset\osnewfile.txt')
#use 'r' before string to avoid issues with escape sequences
print('renamed sucessfully')

# to delete a file
os.remove('D:\\vscode\\py.work\\asset\\delos.txt')
print("Deleted sucessfully")

