#!/bin/python3
from datetime import datetime
name=input("Your Name : ")
age=int(input("Your Age : "))
yr=int((95-age) + datetime.now().year)

print('%s you will turn 95 by the year : %s.' % (name,yr))
