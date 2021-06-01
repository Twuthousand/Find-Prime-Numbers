import time

prev_numbers = [1]

prime_numbers = []

# 100000 runs, Seconds 21.65188

antall_tall = 1000000

start_time=time.time()

for i in range(antall_tall):
    print(f"Progress: {i}/{antall_tall}")
    if len(prev_numbers) == 0:
        prev_numbers.append(i)
    for x in prev_numbers:
        if i%x == 0:
            break
        else:
            continue
    if i != 0:
        prev_numbers.append(i)

    if i%2 == 0:
        continue
    for n in prev_numbers:
        if n == 1:
            continue
        elif n == i:
            prime_numbers.append(i)
            break
        elif i%n == 0:
            break
        else:
            print("!")

            prime_numbers.append(i)
            break

end_time=time.time()-start_time

print(prime_numbers)
print(prev_numbers)
print(f"\nSeconds {end_time:.5f}")

