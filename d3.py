


#!/usr/bin/python3
import  webbrowser 
import os
import  time
import  subprocess
option='''
Press  1  to  open a blank file: 
Press  2  to  play your fav song in youtube :  
Press  3  to  search something  on google   :  
Press  4  to send whatsapp message to your fav number  :  
Press  5  to  check current  time and date  :
press  6  to reboot your machine  : 
'''
print(option)
print(time)
#  taking  input from  user  
#  1 st
choice=input()
#  input function will take input in str  format 
#   conditional  state
if   choice  ==   '5' :
    #   to connect  our BIOS  time 
    current_time=time.ctime()
    print(current_time)

elif  choice  ==  '1'  :
    #   to connect  os level application we use subprocess 
    subprocess.getoutput('gedit')
elif   choice=='2' :
	#to connect to utube

    data=input("type your search :--->  ")
    webbrowser.open_new_tab('https://www.youtube.com/results?search_query='+data)
    

elif  choice  ==  '3' :
    data=input("type your search :--->  ")
    webbrowser.open_new_tab('https://www.google.com/search?q='+data)
elif choice == '6':
    os.system ('reboot')
else  :
    print("hiiii")





