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

##### or #######

tc = int(input())

for x in range(tc):
	n = int(input())
	lst = list(map(int,input().split()))
	lst2 = []
	
	for num in lst:
		if lst.count(num) > 1:
			lst2.append(num)

	new_lst = set(lst) - set(lst2)
	print(list(new_lst))