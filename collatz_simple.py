n = 10000
points = []

while n > 1:
	if n % 2 == 0: 
		n = int(n / 2)
		print(n)
		points.append(n)
	else: 
		n = 3 * n + 1
		print(n)
		points.append(n)
print(points)