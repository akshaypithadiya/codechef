tc = int(input())

for x in range(tc):
	a,b,c,d = map(str, input().split()) # ingredients for first dish
	p,q,r,s = map(str, input().split()) # ingredients for first dish

	d1 = [a,b,c,d] # dish one
	d2 = [p,q,r,s] # dish two

	z = set(d1) & set(d2) # intersection of d1 and d2

	if len(list(z)) >= 2:
		print("similar")
	else:
		print("dissimilar")
