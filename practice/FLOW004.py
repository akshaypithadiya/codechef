t = int(input())

for x in range(t):
	n = int(input())
	rem = n%10
	while (n>0):
		s = n+rem
		n = n//10
	print(s)