def sort_numbers(numbers):
    even = []
    odd = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even, odd

print("----- Even / Odd Sorter -----")

numbers = []

print("Enter 10 numbers:")

for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

even_numbers, odd_numbers = sort_numbers(numbers)

print("\nOriginal List:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)