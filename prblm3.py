'''Problem 3 : 

 take a list say  adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
write the program that will do
  i)  print only those numbers greater than 5
  ii)  also print those numbers those are less than or  equals to 2  ( <= 2 )
  iii)  store these answers in in two different list also
'''
#!/usr/bin/python3
adhoc = [1,2,3,1,4,5,66,22,2,6,0,9]
list1= [i for i in adhoc if i > 5]
list2 = [i for i in adhoc if i <= 2]
print('Numbers greater then 5')
for i in list1:
	print(i)
print(list1)
print('Numbers less than or equals to 2')
for i in list2:
	print(i)
print(list2)
