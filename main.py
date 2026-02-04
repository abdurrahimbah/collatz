# Collatz Conjecture
# Copyright (C) 2026 Abdur Rahim
# Licensed under GPL-3.0-or-later

from collatz import collatz_simple_print
from nth_prime import nth_prime

n = int(input("Hello. Please enter a number: "))
prime_number = nth_prime(n)
print(str(n) + "th prime number is : " + str(prime_number))

print("The Collatz Sequence starting at " + str(prime_number) + " is: ")
collatz_simple_print(prime_number)


