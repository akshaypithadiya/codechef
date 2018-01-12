t = int(input())

for x in range(t):
	z = input().lower()
	
	if (z == "b"):
		print("BattleShip")
	elif (z == "c"):
		print("Cruiser")
	elif (z == "d"):
		print("Destroyer")
	elif (z == "f"):
		print("Frigate")