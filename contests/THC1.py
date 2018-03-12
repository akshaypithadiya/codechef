tc = int(input())

for x in range(tc):
	n = int(input())
	if n%2==0 and n%4==0 and n%8==0:
		print("YES")
	else:
		print("NO")