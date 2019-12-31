def justify(v, k):
	v.append(None)
	mylist = []
	i = 0
	while v[i]!= None:
		w = []
		line = ''
		while len(line)<k:
			if v[i]==None:
				break
			w.append(v[i])
			i += 1
			line = ' '.join(w) 

		if len(line)>k:
			w.pop()
			i -= 1

		if len(w)>1: 
			extraspace = (k-len(''.join(w)))%(len(w)-1)
			s = ' '*extraspace
			w[0] = w[0]+s
			space = ' '*((k-len(''.join(w)))//(len(w)-1))
			mylist.append(space.join(w))
		if len(w)==1:
			mylist.append(w[0])
	mylist[-1] = ' '.join(mylist[-1].split())
	return mylist


v = []
m,n = map(int, input().split())
for i in range(m):
	v.append(input())
print(*justify(v,n),sep="\n")