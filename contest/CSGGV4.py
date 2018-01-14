tc = int(input())

for x in range(tc):
	n = int(input())
	lst = list(map(int,input().split()))
	ans = []

	for i in lst:
		if lst.count(i) == 1:
			ans.append(i)

	for i in ans:
		print(i,end=" ")
	print()