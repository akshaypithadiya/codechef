t = int(input())

lst = list(map(int,input().split()))

even = []
odd = []

for num in lst:
	if num%2==0:
		even.append(num)
	else:
		odd.append(num)

if len(even) > len(odd):
	print("READY FOR BATTLE")
else:
	print("NOT READY")
