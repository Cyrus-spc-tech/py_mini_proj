#importing a nessasary module to intract with operrating system in locam machine 
import os 

#use to print current working directory 
curdir=os.getcwd()
print(curdir)

# change th name of file by path 
os.rename('D:\\vscode\\py.work\\asset\\osfile.txt', 'D:\\vscode\\py.work\\asset\\osnewfile.txt')
#use '\\' to avoid issues with escape sequences

# OR >>  os.rename(r'D:\vscode\py.work\asset\osfile.txt', r'D:\vscode\py.work\asset\osnewfile.txt')
#use 'r' before string to avoid issues with escape sequences
print('renamew sucessfully')
