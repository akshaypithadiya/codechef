tc = int(input())
 
for x in range(tc):
    n = int(input())
    f = list(map(int,input().split()))
    g = list(map(int,input().split()))
    gb = g[::-1]
	
    front=0
    back=0
    i=0
    
    while i!=n:
        if f[i]<=g[i]:
            front+=1
        if f[i]<=gb[i]:
            back+=1
        i+=1
    
    if front==n and back==n:
        print("both")
    elif front==n:
        print("front")
    elif back==n:
        print("back")
    else:
        print("none")