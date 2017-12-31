t = int(input())
for x in range(t):
	n = int(input())
	ld = n%10
	while (n>0):
		s = n+ld
		n = n//10
	print(s)