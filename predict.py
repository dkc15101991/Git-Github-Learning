numbers = [3, 7, 1, 9, 4, 6]

squared = [n**2 for n in numbers if n % 2 == 0]
print("Squared even numbers:", squared)

print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sorted:", sorted(numbers))
