tc = int(input())

for x in range(tc):
	n,m = map(int,input().split())
	ali = list(map(int,input().split()))
	ber = list(map(int,input().split()))

	uni = set(ali) & set(ber)
	print(len(list(uni)))

#solved
