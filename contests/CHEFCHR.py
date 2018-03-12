from itertools import permutations

tc = int(input())

for x in range(tc):
	s = input()
	t = []

	perms = [''.join(p) for p in permutations('chef')]

	for words in perms:

		if words in s:
			t.append(s.count(words))
			
	if len(t)==0:
		print("normal")
	else:
		print("lovely",sum(t))

#solved