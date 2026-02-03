# Collatz Conjecture
# Copyright (C) 2026 Abdur Rahim
# Licensed under GPL-3.0-or-later

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
		

def collatz_simple(n): 
	points = []
	print(n)
	points.append(n)
	while n > 1:
		if n % 2 == 0: 
			n = int(n / 2)
			print(n)
			points.append(n)
		else: 
			n = 3 * n + 1
			print(n)
			points.append(n)
	return points