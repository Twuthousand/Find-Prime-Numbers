# Program that finds prime prev_numbers

"""
There were 9592 prime numbers in the range 100000
Seconds 0.21505

There were 78498 prime numbers in the range 1000000
Seconds 3.51546

There were 664579 prime numbers in the range 10000000
Seconds 358.88098

"""

historical_data = {
"10":"4",
"100":"25",
"1000":"168",
"10000":"1229",
"100000":"9592",
"1000000":"78498",
"10000000":"664579",
}


from math import *
import time
antall_tall = 10000
prev_numbers = [2, ]
prime_numbers = [2, ]

start_time=time.time()
# Creates a loop that the program searches trough for primes.
# Using a method where it eliminates numbers based on previous numbers and if they are factors in the current number.
for i in range(1, antall_tall):
    print(f"{i} / {antall_tall}")
    for n in prev_numbers:
        if n == 1 or i == 1:
            continue
            # Check if n == 1 because we know that 1 is not a prime and every number is dividable by 1.

        elif i%n == 0:
            break
            # This is the main computation of the program which check if the division returns any rest.
            # If it returns 0 it means it is divisable by a number in prev_numbers which is not itself and is therfor not a prime number.

        elif n == prev_numbers[-1]:
            prime_numbers.append(i)
            prev_numbers.append(i)
            break
            # If the current number has not been eliminated by now it is a prime number.

        elif n+1>sqrt(i):
            prime_numbers.append(i)
            prev_numbers.append(i)
            break
            # Also if n is higher than the squareroot of i then all the factor have already been tried and i is a prime number.
        else:
            continue


end_time=time.time()-start_time

print(prime_numbers)
print(f'There were {len(prime_numbers)} prime numbers in the range {antall_tall}')
print(f"\nSeconds {end_time:.5f}")
