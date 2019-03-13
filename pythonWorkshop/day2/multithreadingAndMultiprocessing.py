# import sys
# import random
# import time
# from threading import Thread
from mulitprocessing import Process

# size = 1000000
# threads = 2
# myList = []

# [[] for i in range(threads)]

# def func(count, myList):
# 	[myList.append(random.random()) for i in range(count)]


# # def multithreading():
# # 	jobs = []
# # 	for i in range(0, threads):
# # 		thread = Thread(target=func, args=(size, myList[i]))
# # 		jobs.append(thread)

# # 	for i in jobs:
# # 		i.start()
# # 	for i in jobs:
# # 		i.join()

# def multithreading():
# 	jobs = []
# 	for i in range(0, threads):
# 		process = Process(target=func, args=(size, myList[i]))
# 		jobs.append(process)

# 	for i in jobs:
# 		i.start()
# 	for i in jobs:
# 		i.join()

# a = time.time()
# multithreading()
# b = time.time()
# print(b-a)

# # print([i for i in range(10000,99999)])
# '''

# venv
# 0mysql
# 0redis
# 0aws
# 0razerpay

# '''
# if __name__=='__main__':
# 	print(sys.argv[1], sys.argv[2])
# 	#do something
# 	#else pass


# anshuman tripathi 1996-97


# S/W Design Patterns
# 1. Decorator- s/w design pattern 
# 2. Decorators dynamically alter the functionality of a funtion 
# without chaning the source code of the funtion being decorated.
# 3. Functions are object in python which allows--
# 	a. To accept function objects as arguments
# 	b. Allow to return functions objects as return values



def findPass(r):
	a = [i for i in range(r)]
	return a

def captivePortal():
	global threads
	jobs = []
	for i in range(threads):
		process = Process(target=findPass, args=(r,))
		jobs.append(process)
	
	for i in jobs:
		i.start()
	for i in jobs:
		i.join()

print(captivePortal())
