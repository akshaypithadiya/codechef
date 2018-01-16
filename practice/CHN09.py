t = int(input())

for x in range(t):
	s = input()
	lst = list(s)
	a = lst.count('a')
	b = lst.count('b')

	if a<b:
		print(a)
	else:
		print(b)
