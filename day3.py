# input 2 numbers

# print prime number between start and end
start, end = input('give 2 numbers : ').split()
if end < start:
    start, end = end, start

for divide in range(int(start), int(end)):
    # is_prime = True
    if divide == 1:
        continue
    for k in range(2, divide):
        if divide % k == 0:
            # is_prime = False
            break
    # if is_prime:
    else:
        print(divide, end=" ")