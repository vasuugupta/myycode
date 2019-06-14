'''
Problem 6: 

 use file handling to create a linux command  similar to cat .
  test at least  4 cases and options of cat command
 compare the difference of cat command and post the result
'''

import time

option='''
1. TO VIEW A FILE
2. TO CREATE  A FILE
3. TO COPY DATA FROM ONE FILE TO ANOTHER
4. TO WRITE IN A FILE
'''
print(option)
print ("enter your choice ::")
comm=input()
if comm == '1':
	f_name=input("enter a file name=")
	f=open(f_name,'r')
	print(f.read())
elif comm =='2':
	f_name=input("enter a file name=")
	f=open(f_name,'w')
	f_name=input("enter a file name")
	#data=input("enter data without pressing enter=")
	#f.write(data)
elif comm=='3':
	f_name=input("enter a file name whose content to be copied=")
	f=open(f_name,'r')
	data=f.read()
	f_name1=input("enter a file name in which data is to be copied=")
	f=open(f_name1,'a+')
	print('\n')
	f.write(data)
	f.seek(0)
	print('\n')
	print(f.read())
elif comm=='4':
	f_name = input('Enter file name: ')
	fhand = open(f_name,'a')
	text = input('Enter what you want to write: ')
	fhand.write(text)
	fhand.close()
