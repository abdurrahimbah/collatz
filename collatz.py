def collatz(n, collatz_points = None):
	
	if collatz_points is None:
		collatz_points = []
		
	if n == 1:
		return collatz_points
		
	elif n % 2 != 0:
		collatz_points.append(3 * n + 1)
		return collatz(3 * n + 1,  collatz_points)
		
	elif n % 2 == 0:
		collatz_points.append(n // 2)
		return collatz(n // 2, collatz_points)