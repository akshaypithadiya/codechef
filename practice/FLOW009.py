t = int(input())

for x in range(t):
	a,b = map(int,input().split())

	if(a>1000):
		exp = (a*b)-(a*b)/10
		print("%0.6f"%exp)
	else:
		exp = a*b
		print("%0.6f"%exp)