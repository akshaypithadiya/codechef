tc = int(input())

for x in range(tc):
	t = 0
	n = int(input())
	while(n>0):
		d=n%10
		t=t+d
		n=n//10
	print(t)
