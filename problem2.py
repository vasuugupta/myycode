
#!/usr/bin/python3
import time
from googlesearch import search
web=input("plzz enter topic==")
#time to search
url=[]
for i in search(web, stop=5):

	print (i)
 #i will only print url
	time.sleep(1)
	url.append(i)
print (url)

