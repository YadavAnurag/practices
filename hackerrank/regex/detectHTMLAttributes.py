import sys
import re

n = int(input())
s = ''
for i in range(n):
	s+=input()

tags = list(set((re.findall('<[a-z]+ [a-z]+="', s))))
print(tags)

# for tag in tags:
# 	pattern = tag+
# 	attr = re.findall()

re.search('\xanura attribute to find ')

