import os 
import numpy as np 

print(os.getpid())

pid = os.fork() 

if pid == 0 :
	print(os.getpid())
else:
	print(os.getpid())