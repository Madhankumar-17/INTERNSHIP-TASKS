def times_table(n):
    print(f"\nMultiplication Table of {n}")
    print("--------------------------")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

print("----- Multiplication Table Generator -----")

for i in range(3):
    number = int(input(f"\nEnter number {i+1}: "))
    times_table(number)