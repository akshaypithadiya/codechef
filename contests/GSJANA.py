tc = int(input())

for x in range(tc):
	r,n,s,e,w = map(int,input().split())
	lst = [r,n,s,e,w]
	if lst.count(r)>=2:
		print("YES")
	else:
		print("NO")