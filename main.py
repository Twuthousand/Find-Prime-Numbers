prev_numbers = []

prime_numbers = []

for i in range(1, 100):
    prev_numbers.append(i)
    for n in prev_numbers:
        if n == 1:
            continue
        elif n == i:
            prime_numbers.append(i)
            break
        elif i%n == 0:
            break

print(prime_numbers)



