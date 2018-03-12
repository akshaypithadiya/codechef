tc = int(input())

for x in range(tc):
	n = int(input())
	ls = list(map(int,input().split()))

	s1 = ls[0::2]
	s2 = ls[1::2]

	s1.sort()
	s2.sort()

	c1=0
	c2=0

	while s1 and s2:

		high_card_s1 = s1.pop()
		high_card_s2 = s2.pop()

		if high_card_s1 > high_card_s2:
			c1+=1
		else:
			c2+=1

	if c1>c2:
		print("1")
	elif c1==c2:
		print("draw")
	else:
		print("2")

#solved