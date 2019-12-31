
import sys
import re 

s = ''.join(sys.stdin.readlines())

if re.search('#include<stdio.h>', s):
    print('C')
elif re.search('public static void main(', s):
    print('Java')
else:
    print('Python')

