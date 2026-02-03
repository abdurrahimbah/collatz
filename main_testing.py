# Collatz Conjecture
# Copyright (C) 2026 Abdur Rahim
# Licensed under GPL-3.0-or-later

from collatz import collatz, collatz_simple
from nth_prime import nth_prime

print("Welcome to to the Collatz project written by Abdur Rahim. You have two options. ")
print("Option 1: Enter an integer to compute the Collatz sequence starting from it.")
print("Option 2: Enter an integer (n) to find nth prime number and compute the Collatz sequence starting from the prime number.")

choice = input("Choose your option, collatz or prime_collatz: ")
if (choice == "2"): 
	n = int(input("Please enter a number: "))
	prime_number = nth_prime(n)
	print(str(n) + "th prime number is : ")
	print("The Collatz sequence atarting at " + str(prime_number) + " is: ")
	collatz_simple(prime_number)
elif choice == "1": 
	n = int(input("Please enter a number: "))
	print("The Collatz sequence starting at " + str(n) + " is: ")
	collatz_simple(n)
else: 
	print("See you.")





