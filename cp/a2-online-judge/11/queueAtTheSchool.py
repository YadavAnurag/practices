n, t = map(int, input().split())
queue = input()

for _ in range(t):
	queue = queue.replace('BG', 'GB')
print(queue)