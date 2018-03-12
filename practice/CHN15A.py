tc = int(input())

for x in range(tc):
	n,k = map(int,input().split())
	ls = list(map(int,input().split()))

	ns = [num+k for num in ls]

	count = 0

	for n in ns:
		if n%7==0:
			count+=1
	print(count)
