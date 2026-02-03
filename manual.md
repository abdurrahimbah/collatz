# Just open the project in terminal and run 

python3 main.py or
python3 main_testing.py # if you want to test the latest additions

# If you want to use the terminal interface, open the project path in terminal, then you can

python3
from collatz import collatz
from nth_prime import nth_prime
nth_prime(100) # prints 100th prime number
collatz(100) # prints the Collatz sequence starting at 100
collatz(nth_prime(100)) # prints the Collatz sequence starting at the 100th prime number.