tc = int(input())

for x in range(tc):
	n = int(input())
	temp = n
	rev = 0

	while (n>0):
		rem=n%10
		rev=(rev*10)+rem
		n=n//10

	if (rev==temp):
		print("wins")
	else:
		print("losses")
