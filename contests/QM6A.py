tc = int(input())

for x in range (tc):
	n = int(input())

	lst=[]
	rlst=[]

	for i in range(1,n+1):
		lst.append(i)
		rlst.append(i)

	rlst.pop()
	rlst.reverse()
	nlst = lst + rlst

	sqlst = [z**2 for z in nlst]
	s = sum(sqlst)
	print(s)