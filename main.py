// Collatz Conjecture
// Copyright (C) 2026 Abdur Rahim
// Licensed under GPL-3.0-or-later

from collatz import collatz
from nth_prime import nth_prime

n = int(input("Hello. Please enter a number: "))
prime_number = nth_prime(n)
print(str(n) + "th prime number is : " + str(prime_number))

points = collatz(prime_number)
print(points)


