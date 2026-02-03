Collatz Conjecture 
Copyright (C) 2026 Abdur Rahim 
Licensed under GPL-3.0-or-later 

# Example usage

python3 main.py or
python3 main_testing.py # if you want to test the latest additions

# Example usage (at first, run "python3")

from collatz import collatz, collatz_simple
from nth_prime import nth_prime
nth_prime(100) # prints 100th prime number
collatz(100) # prints the Collatz sequence starting at 100 using collatz() function
collatz_simple(100) # prints the Collatz sequence starting at 100 using collatz_simple() function
collatz(nth_prime(100)) # prints the Collatz sequence starting at the 100th prime number.
collatz_simple(nth_prime(100)) # prints the Collatz sequence starting at the 100th prime number.



