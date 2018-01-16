t = int(input())

for x in range(t):
	a,b,c = map(int,input().split())
	lst = [a,b,c]
	lst.sort()
	print(lst[-2])
