t = int(input())
 
for x in range(t):
	s = input()
	lst = list(s)
 
	a = lst[:len(lst)//2]
	b = lst[len(lst)//2:]
	a.sort()
	b.sort()
	
	if len(lst)%2==0:
		if a==b:
			print("YES")
		else:
			print("NO")
 
	elif len(lst)%2!=0:
 
		mid = (len(lst)-1)//2
		idx = lst.index(lst[mid])
		rem = lst.pop(idx)
		
		a = lst[:len(lst)//2]
		b = lst[len(lst)//2:]
		a.sort()
		b.sort()
 
		if a==b:
			print("YES")
		else:
			print("NO")