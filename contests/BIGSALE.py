t = int(input())
 
for x in range(t):
 
	n = int(input())
 
	total_loss = []
 
	for i in range(n):
		pqd = list(map(int,input().split()))
 
		price = pqd[0]
		quantity = pqd[1]
		discount = pqd[2]
 
		incr_price = price + price*discount/100
		decr_price = incr_price*discount/100
		final_price = incr_price-decr_price
		loss = (price - final_price)*quantity
		total_loss.append(loss)
	print(sum(total_loss))