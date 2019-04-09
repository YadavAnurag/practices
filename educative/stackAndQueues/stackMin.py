stack = []
alt = []

def push(val):
	stack.append(val)
	if len(alt) == 0:
		alt.append(val)
		print('append')
		return
	print('stack', stack, alt)
	print('checking',alt[-1]>val)
	if alt[-1] > val:
		alt.append(val)
		return

def pop():
	if len(stack) == 0:
		return None
	a = stack.pop()
	if alt[-1] == a:
		alt.pop()
	return a

def min():
	if len(alt) == 0:
		return None
	return alt[-1]