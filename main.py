# Program that finds prime prev_numbers
# It's the first generation and there will be a faster one with optimizations. -> main_faster.py

"""
There were 9592 prime numbers in the range 100000
Seconds 40.36697


"""

prev_numbers = []
prime_numbers = []
antall_tall = 1000
import time
start_time=time.time()
# Creates a loop that the program searches trough for primes.
# Using a method where it eliminates numbers based on previous numbers and if they are factors in the current number.
for i in range(1, antall_tall):
    print(f"{i} / {antall_tall}")
    prev_numbers.append(i)
    for n in prev_numbers:
        if n == 1:
            continue
            # Check if n == 1 because we know that 1 is not a prime and every number is divisable by 1.
        elif n == i:
            prime_numbers.append(i)
            break
            # If the current number has not been eliminated by now it is a prime number.
        elif i%n == 0:
            break
            # this is the main computation of the program which check if the division returns any rest.
            # if it returns 0 it means it is divisable by a number in prev_numbers which is not itself and is therfor not a prime number.

print(prime_numbers)
print(len(prime_numbers))
end_time=time.time()-start_time

print(f'There were {len(prime_numbers)} prime numbers in the range {antall_tall}')
print(f"\nSeconds {end_time:.5f}")
