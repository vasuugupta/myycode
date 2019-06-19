'''
Problem 8: 

write a code that will take input from a user and check that if it is a command
then execute it with following  conditions :

 i)  all the commands given by user either wrong or right must be store in a file
ii)   output of success command will be shown to monitor
iii)  if the input command is repeated by user give him voice note not to do this again
'''
#!/usr/bin/python3

import os
from gtts import gTTS
cmd=input("Enter the command:-")
os.system("touch commands.txt")
statinf=os.path.getsize("commands.txt")
a=os.system(cmd +" 2>/dev/null")
if a==0:
	if statinf == 0:
		f=open("commands.txt","w+")
		f.write(cmd+" \n")
		f.close()
	else:
		f=open("commands.txt","a+")
		f.seek(0)
		lines=f.read().split("\n")
		command=cmd+" "
		if command in lines:
			tts = gTTS(text="do not repeat the command", lang='en')			  
			tts.save("comd.mp3")
			os.system("xdg-open comd.mp3 ")
			
		else:
			pass
		f.write(cmd+" \n")
		f.close()
else:
	print("Wrong command!")
	f=open("commands.txt","a+")
	f.write(cmd+" \n")
	f.close()


