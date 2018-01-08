tc = int(input())

for x in range(tc):
	a,b,c,d = map(int, input().split())
	
	lst = [a,b,c,d]
	lst.sort()

	a=lst[0]
	b=lst[1]
	c=lst[2]
	d=lst[3]

	if a==b and c==d:
		print("YES")
	else:
		print("NO")
