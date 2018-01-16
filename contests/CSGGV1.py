#  Code Sense

tc = int(input())

for x in range(tc):
	n = int(input())
	tmp = n
	p = 1

	while(n>0):
		p = p*(n%10)
		n = n//10

	seed = tmp*p

	print(seed)
    

