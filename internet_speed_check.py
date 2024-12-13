# Python program to test 
# internet speed 

import speedtest 


st = speedtest.Speedtest() 

option = int(input('''What speed do you want to test:\n
1) Download Speed\n 
2) Upload Speed \n
3) Ping \n
Your Choice: ''')) 

if option == 1: 
	print(st.download()) 
elif option == 2: 
	print(st.upload()) 
elif option == 3: 
	servernames =[] 
	st.get_servers(servernames) 
	print(st.results.ping) 
else: 
	print("Please enter the correct choice !") 
