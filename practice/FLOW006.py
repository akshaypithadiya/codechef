tc = int(input())

for x in range(tc):
	total = 0
	n = int(input())

	while(n>0):
		rem = n%10
		total = total+rem
		n=n//10
		
	print(total)
