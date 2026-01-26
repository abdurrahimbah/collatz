# Collatz Conjecture
# Copyright (C) 2026 Abdur Rahim
# Licensed under GPL-3.0-or-later

def is_prime(num): # tests if the input number is prime
    if num < 2:
        return False # number less than 2 is not prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n): # outputs nth prime number using is_prime() function
    count = 0 # stores the number of total prime numbers we have already found
    num = 2 # start from the first prime number

    while True:
        if is_prime(num):
            count += 1 # increase the count if the passed number is prime
            if count == n: # terminate the loop once we have found nth prime
                return num
        num += 1