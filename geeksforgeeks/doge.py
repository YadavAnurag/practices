# s = input()
# def doge(str):
# 	count=0
# 	for i in range(len(str)-2):
# 		if(str[i]=='d' and str[i+1]=='o' and str[i+3]=='e'):
# 			count+=1
# 	# count,l=0,[]
# 	# while(str.find('do')!=-1):
# 	# 	t = str[str.find('do'):str.find('do')+4]
# 	# 	if len(t)==4:
# 	# 		l.append(t)
# 	# 		str = str.replace('do','',1)
# 	# for i in l:
# 	# 	if(i[-1]=='e'):
# 	# 		count+=1
# 	return count
# print(doge(s))



# {
# #Initial Template for Python 3
# //Position this line where user code will be pasted.
# import re
# def main():
#     testcases=int(input()) #testcases
#     while(testcases>0):
#         str=input()
#         imgExtracter(str)
#         testcases-=1
        
# if __name__=='__main__':
#     main()
# }

# ''' Please note that it's Function problem i.e.
# you need to write your solution in the form of Function(s) only.
# Driver Code to call/invoke your function is mentioned above. '''

# #User function Template for python3
# def imgExtracter(s):
#     if(s.find('<img src=')):
#         start = s.find('<img src=')+10
#         end = s.find('.jpg')+4
#         print(s[start:end])
#     else:
#         print(-1)

n=3
while(n):
	s = input()
	print(s)
	n -= 1