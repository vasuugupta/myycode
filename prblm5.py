
'''
Problem 5:

write a code  will take  input as your name and greet you with
good morning , good evening , goodafter noon , good night as per the current time your system:
'''

#!/usr/bin/Python3
import datetime
current_time = datetime.datetime.now()
if current_time.hour < 12:
   print('Good morning.')
elif 12 <= current_time.hour < 18:
   print('Good afternoon.')
else:
   print('Good evening.')

